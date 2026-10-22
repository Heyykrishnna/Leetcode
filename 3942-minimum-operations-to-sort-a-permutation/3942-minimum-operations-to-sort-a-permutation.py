class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        p = nums.index(0)
        if n <= 1:
            return 0

        inc = True
        for i in range(n):
            if nums[(p + i) % n] != i:
                inc = False
                break

        dec = True
        for i in range(n):
            if nums[(p - i) % n] != i:
                dec = False
                break

        if not inc and not dec:
            return -1

        if inc:
            ans = min(ans, p, 1 + (n - p) % n + 1)
        if dec:
            ans = min(ans, 1 + (p + 1) % n, (n - 1 - p) % n + 1)

        return ans