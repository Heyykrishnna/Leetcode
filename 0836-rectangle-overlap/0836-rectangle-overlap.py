class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        xo = rec1[0] < rec2[2] and rec2[0] < rec1[2]
        yo = rec1[1] < rec2[3] and rec2[1] < rec1[3]
        return xo and yo