class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(1, n + 1):
            for w in wordDict:
                k = len(w)
                if i >= k and dp[i - k] and s[i - k:i] == w:
                    dp[i] = True
                    break
                    
        return dp[n]