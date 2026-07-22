class Solution:
    def getRow(self, x: int) -> List[int]:
        row = [1]

        for i in range(1, x + 1):
            ans = row[i - 1] * (x - i + 1) // i
            row.append(ans)

        return row