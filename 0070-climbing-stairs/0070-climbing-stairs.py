class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        pre = 1
        pree = 2

        for i in range(3, n+1):
            curr = pre + pree
            pre = pree
            pree = curr
        
        return pree