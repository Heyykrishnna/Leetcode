# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        le = 1
        ri = n
        
        while le < ri:
            mid = (le+ri) // 2
            if isBadVersion(mid):
                ri = mid
            else:
                le = mid + 1
            
        return le