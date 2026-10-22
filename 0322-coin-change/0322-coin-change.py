class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in coins:
            for x in range(i, amount + 1):
                dp[x] = min(dp[x], dp[x - i] + 1)

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1