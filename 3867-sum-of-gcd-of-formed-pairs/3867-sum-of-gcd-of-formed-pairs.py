class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gc(a, b):
            while b:
                a, b = b, a % b
            return a
        
        pre = []
        cu = 0

        for i in nums:
            if i > cu:
                cu = i
            pre.append(gc(i, cu))
        
        pre.sort()
        su = 0
        le, ri = 0, len(pre) - 1

        while le < ri:
            su += gc(pre[le], pre[ri])
            le += 1
            ri -= 1
        
        return su