class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        le = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[le] = nums[le], nums[i]
                le += 1
            
        return nums