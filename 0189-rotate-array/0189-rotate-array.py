class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        for i in range (k):
            la = nums.pop()
            nums.insert(0, la)