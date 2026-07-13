import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        su = n * (n + 1) // 2
        x = math.isqrt(su)

        if x * x == su:
            return x
        else:
            return -1
