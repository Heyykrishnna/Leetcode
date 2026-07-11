class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        le, ri = 1, x
        ans = 0

        while le <= ri:
            mid = (le + ri) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                ans = mid
                le = mid + 1
            else:
                ri = mid - 1
            
        return ans