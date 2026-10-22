class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            cur = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = dp[j - 1]
                else:
                    cur[j] = 1 + min(dp[j], cur[j - 1], dp[j - 1])
            dp = cur
            
        return dp[n]