class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and grid[r][c] > 0):
                return 0
            total = grid[r][c]
            grid[r][c] = 0 
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                total += dfs(r + dr, c + dc)
                
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if dfs(i, j) % k == 0:
                        ans += 1
                        
        return ans