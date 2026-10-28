class Solution:
    def canJump(self, nums: list[int]) -> bool:
        fin = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= fin:
                fin = i
            
        if fin == 0:
            return True
        else:
            return False
