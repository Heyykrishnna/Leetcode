class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = [set() for _ in grid[0]]
        dp[0].add(0)

        for row in grid:
            for j, num in enumerate(row):
                prev = dp[j].copy()

                if j > 0:
                    prev |= dp[j - 1]

                dp[j] = {x ^ num for x in prev}

        return min(dp[-1])