class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        pos = set()
        neg = set()
        ans = []
        bo = [['.'] * n for i in range(n)]
        col = set()

        def f(r):
            if r == n:
                cp = [''.join(row) for row in bo]
                ans.append(cp)
                return
            
            for c in range(n):
                if c in col or (r + c) in pos or (r -c) in neg:
                    continue
                
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                bo[c][r] = 'Q'

                f(r+1)

                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                bo[c][r] = '.'

        f(0)
        return ans