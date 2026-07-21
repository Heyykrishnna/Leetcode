class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        oe = s.count('1')
        ze = [len(z) for z in s.replace('1', ' ').split()]

        ans = 0
        for i in range(len(ze) - 1):
            ans = max(ans, ze[i] + ze[i+1])
            
        return oe + ans