class Solution:
    def minimumPushes(self, word: str) -> int:
        cu = [0] * 26
        for c in word:
            cu[ord(c) - ord('a')] += 1
        
        cu.sort(reverse=True)
        ans = 0
        dis = 0
        for i in cu:
            ans += i * (1+dis//8)
            dis += 1
        
        return ans