class Solution:
    def canJump(self, nums: list[int]) -> bool:
        ma = 0
        for i in range(0, len(nums)):
            if i > ma:
                return False
            
            ma = max(ma, i + nums[i])
        
        return True