class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        a = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue                
            l, r = i + 1, n - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    a.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return a