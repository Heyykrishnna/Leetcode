class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        le = 0
        ri = 0
        cu = 0

        while le < n and ri < m:
            if g[le] <= s[ri]:
                cu += 1
                le += 1
            ri += 1

        return cu