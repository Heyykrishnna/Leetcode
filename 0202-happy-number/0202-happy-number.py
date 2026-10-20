class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1 and n not in s:
            s.add(n)
            t = 0
            for i in str(n):
                t += (int(i) ** 2)
            n = t
            
        return n == 1