class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s = sum(nums)
        m = max(nums)
        return len(nums) * m - s