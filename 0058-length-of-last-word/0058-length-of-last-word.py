class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        le = 0
        n = len(s) - 1
        
        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':
            le += 1
            n -= 1
        
        return le