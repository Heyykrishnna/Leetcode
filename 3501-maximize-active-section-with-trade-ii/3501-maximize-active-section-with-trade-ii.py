class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        tot = s.count('1')
        b = []
        st_idx = 0
        
        for i in range(1, n):
            if s[i] != s[i-1]:
                b.append((int(s[st_idx]), st_idx, i - 1, i - st_idx))
                st_idx = i
        b.append((int(s[st_idx]), st_idx, n - 1, n - st_idx))
        
        m = len(b)
        fg = [0] * m
        for i in range(1, m - 1):
            if b[i][0] == 1:
                fg[i] = b[i-1][3] + b[i+1][3]
                
        L_log = m.bit_length()
        st = [[0] * L_log for _ in range(m)]
        for i in range(m):
            st[i][0] = fg[i]
            
        for j in range(1, L_log):
            for i in range(m - (1 << j) + 1):
                st[i][j] = max(st[i][j-1], st[i + (1 << (j - 1))][j-1])
                
        def q_st(l, r):
            if l > r: return 0
            k = (r - l + 1).bit_length() - 1
            return max(st[l][k], st[r - (1 << k) + 1][k])
            
        b_st = [x[1] for x in b]
        
        def get_idx(val):
            l, r = 0, m
            while l < r:
                mid = (l + r) // 2
                if b_st[mid] <= val:
                    l = mid + 1
                else:
                    r = mid
            return l - 1

        ans = []
        for ql, qr in queries:
            L = get_idx(ql)
            R = get_idx(qr)
            
            if R - L < 2:
                ans.append(tot)
                continue
                
            mx = 0
            if b[L+1][0] == 1:
                ll = b[L][2] - ql + 1
                rl = (qr - b[R][1] + 1) if L + 2 == R else b[L+2][3]
                mx = max(mx, ll + rl)
                
            if R - 1 > L + 1 and b[R-1][0] == 1:
                ll = b[R-2][3]
                rl = qr - b[R][1] + 1
                mx = max(mx, ll + rl)
                
            if R - 2 >= L + 2:
                mx = max(mx, q_st(L + 2, R - 2))
                
            ans.append(tot + mx)
            
        return ans