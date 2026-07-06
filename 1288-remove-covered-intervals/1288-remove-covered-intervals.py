class Solution:
    def removeCoveredIntervals(self, i: List[List[int]]) -> int:
        i.sort(key=lambda x: (x[0], -x[1]))
        res = r = 0

        for st, end in i:
            res += end > r
            r = max(r, end)

        return res