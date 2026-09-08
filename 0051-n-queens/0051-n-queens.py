class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def f(row, cols, ar1, ar2, board):
            if row == n:
                res.append(list(board))
                return
            for col in range(n):
                if col in cols or (row - col) in ar1 or (row + col) in ar2:
                    continue
                cols.add(col)
                ar1.add(row - col)
                ar2.add(row + col)
                board.append("." * col + "Q" + "." * (n - 1 - col))
                
                f(row + 1, cols, ar1, ar2, board)
                
                board.pop()
                ar2.remove(row + col)
                ar1.remove(row - col)
                cols.remove(col)

        res = []
        f(0, set(), set(), set(), [])
        return res