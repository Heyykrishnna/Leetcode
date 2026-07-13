class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        re = 0

        for i in range(1, k + 1):
            re = (re * 10 + 1) % k
            if re == 0:
                return i

        return -1
