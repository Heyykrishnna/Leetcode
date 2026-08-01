class Solution:
    def predictTheWinner(self, x: List[int]) -> bool:
        n = len(x)
        if not n & 1: return True

        @cache
        def maxDiff(i: int, j: int) -> int:
            if i == j: return x[i]
            return max(x[i] - maxDiff(i + 1, j),
                       x[j] - maxDiff(i, j - 1))

        return maxDiff(0, n - 1) >= 0