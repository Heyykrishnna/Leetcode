class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mc = 0        
        
        for i in range(n):
            cu = 0
            for j in range(i, n):
                if nums[j] == target:
                    cu += 1
                else:
                    cu -= 1
                if cu > 0:
                    mc += 1
                    
        return mc