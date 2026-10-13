class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def f(i):
            prev1 = 0
            prev2 = 0
            for x in i:
                cur = max(prev1, prev2 + x)
                prev2 = prev1
                prev1 = cur
            return prev1
            
        return max(f(nums[:-1]), f(nums[1:]))