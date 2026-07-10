class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        a = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n

        for i in range(n):
            pos[a[i]] = i

        arr = [nums[i] for i in a]
        nxt = [0] * n
        x = 0

        for i in range(n):
            x = max(x, i)

            while x + 1 < n and arr[x + 1] - arr[i] <= maxDiff:
                x += 1

            nxt[i] = x

        log = n.bit_length()
        com = [nxt]

        for i in range(1, log):
            pre = com[i - 1]
            com.append([pre[pre[j]] for j in range(n)])

        res = []

        for q in queries:
            j = pos[q[0]]
            x = pos[q[1]]

            if j > x:
                j, x = x, j

            if j == x:
                res.append(0)
                continue

            coi = 0
            cur = j

            for i in range(log - 1, -1, -1):
                if com[i][cur] < x:
                    cur = com[i][cur]
                    coi += 1 << i

            if nxt[cur] >= x:
                res.append(coi + 1)
            else:
                res.append(-1)

        return res