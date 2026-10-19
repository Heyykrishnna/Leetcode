class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = sorted(nums1 + nums2)
        n = len(arr)
        mid =(n // 2)
        
        if n%2==1:
            return float(arr[mid])
        return (arr[mid - 1] + arr[mid]) / 2.0