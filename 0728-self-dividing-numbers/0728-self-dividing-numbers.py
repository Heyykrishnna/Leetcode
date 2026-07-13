class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def f(n):
            temp = n
            while temp > 0:
                dig = temp % 10
                
                if dig == 0 or n % dig != 0:
                    return False
                temp //= 10
            return True
        
        return [n for n in range(left, right + 1) if f(n)]