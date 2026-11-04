class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        c = nums[0] + nums[1] + nums[2]
        n = len(nums)
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s-target) < abs(c-target):
                    c = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s    
        return c