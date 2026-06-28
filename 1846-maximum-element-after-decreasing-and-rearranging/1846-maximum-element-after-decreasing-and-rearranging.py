class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        for i in arr:
            ans = min(ans + 1, i)
        
        return ans