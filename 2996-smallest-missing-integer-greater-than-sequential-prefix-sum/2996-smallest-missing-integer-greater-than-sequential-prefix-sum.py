class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        se = set(nums)
        su = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                su += nums[i]
            else:
                break

        while su in se:
            su += 1
        
        return su