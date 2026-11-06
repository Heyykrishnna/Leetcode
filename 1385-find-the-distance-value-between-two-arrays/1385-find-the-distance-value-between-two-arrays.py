class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for x in arr1:
            lo, hi = 0, len(arr2)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr2[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid

            i = lo
            if (i < len(arr2) and arr2[i] - x <= d) or (i > 0 and x - arr2[i - 1] <= d):
                continue
            ans += 1

        return ans