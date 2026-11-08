class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rr, ccc = len(grid), len(grid[0])
        rc = [sum(row) for row in grid]
        cc = [sum(grid[r][c] for r in range(rr)) for c in range(ccc)]
        
        ans = 0
        for i in range(rr):
            for j in range(ccc):
                if grid[i][j] == 1 and (rc[i] > 1 or cc[j] > 1):
                    ans += 1
        return ans