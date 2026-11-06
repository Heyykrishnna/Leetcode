class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        logs.sort(key=lambda l: l[1])
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])

        counts = [0] * (n + 1)
        active = 0
        left = 0
        right = 0
        ans = [0] * len(queries)

        for i, q in indexed_queries:
            while right < len(logs) and logs[right][1] <= q:
                s = logs[right][0]
                if counts[s] == 0:
                    active += 1
                counts[s] += 1
                right += 1

            while left < len(logs) and logs[left][1] < q - x:
                s = logs[left][0]
                counts[s] -= 1
                if counts[s] == 0:
                    active -= 1
                left += 1

            ans[i] = n - active

        return ans
