class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        ro, co = len(grid), len(grid[0])
        md = {(0, 0): grid[0][0]}
        qu = [(0, 0, grid[0][0])]
        he = 0  
        
        while he < len(qu):
            r, c, dm = qu[he]
            he += 1  
            if dm >= health:
                continue
                
            if r == ro - 1 and c == co - 1:
                return True
                
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ro and 0 <= nc < co:
                    nd = dm + grid[nr][nc]
                    
                    if nd < md.get((nr, nc), float('inf')):
                        md[(nr, nc)] = nd
                        qu.append((nr, nc, nd))
                        
        return False