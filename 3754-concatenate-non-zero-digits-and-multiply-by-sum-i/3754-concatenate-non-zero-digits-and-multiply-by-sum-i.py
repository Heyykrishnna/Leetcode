class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nu = str(n).replace('0', '')
        
        if not nu:
            return 0
        x = int(nu)
        ans = sum(int(digit) for digit in nu)        

        return x * ans