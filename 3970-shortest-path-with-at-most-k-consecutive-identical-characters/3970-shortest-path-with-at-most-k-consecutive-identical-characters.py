import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            
        d = [[float('inf')] * (k + 1) for _ in range(n)]
        d[0][1] = 0
        q = [(0, 0, 1)]
        
        while q:
            w, u, c = heapq.heappop(q)
            
            if w > d[u][c]:
                continue
            if u == n - 1:
                return w
                
            for v, cost in g[u]:
                nc = c + 1 if labels[u] == labels[v] else 1
                if nc <= k and w + cost < d[v][nc]:
                    d[v][nc] = w + cost
                    heapq.heappush(q, (w + cost, v, nc))
                    
        return -1