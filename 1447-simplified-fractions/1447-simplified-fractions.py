class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        def f(a, b):
            while b:
                a, b = b, a % b
            return a
        
        r = []
        for j in range(2, n + 1):
            for i in range(1, j):
                if f(i, j) == 1:
                    r.append(f"{i}/{j}")
        return r