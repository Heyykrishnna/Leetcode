class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        c = 0
        m = nums[0]
        for n in nums:
            c = max(n, c + n)
            m = max(m, c)
        return m