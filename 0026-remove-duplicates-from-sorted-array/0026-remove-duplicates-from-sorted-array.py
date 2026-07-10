class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        le = 0

        for i in range(len(nums)):
            if nums[le] != nums[i]:
                le += 1
                nums[le], nums[i] = nums[i], nums[le]
            
        return le+1
