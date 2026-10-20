class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = 0

        def f(a, b):
            m = len(a)
            if m <= 1:
                return a == b
            
            p = 0
            while p + 1 < m and a[p] <= a[p + 1]:
                p += 1
            
            if p == m - 1:
                return a == b
            
            split = p + 1
            return a[split:] + a[:split] == b

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            for i in range(0, n, k):
                if not f(nums[i : i + k], s[i : i + k]):
                    valid = False
                    break

            if valid:
                ans += k

        return ans