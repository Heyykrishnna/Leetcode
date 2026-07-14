from functools import cache
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        @cache
        def f(i, g1, g2):
            if i == n:
                if g1 != 0 and g1 == g2:
                    return 1
                else:
                    return 0

            ans = f(i + 1, g1, g2)

            ng1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans = (ans + f(i + 1, ng1, g2)) % mod

            ng2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans = (ans + f(i + 1, g1, ng2)) % mod

            return ans

        return f(0, 0, 0)
