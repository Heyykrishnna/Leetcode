class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        idg = [0] * n
        
        for u, v, w in edges:
            adj[u].append((v, w))
            idg[v] += 1
            
        tu = [i for i in range(n) if idg[i] == 0]
        for u in tu:
            for v, _ in adj[u]:
                idg[v] -= 1
                if idg[v] == 0:
                    tu.append(v)
        
        def check(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in tu:
                if dist[u] == float('inf') or not online[u]:
                    continue
                for v, w in adj[u]:
                    if w >= mid:
                        dist[v] = min(dist[v], dist[u] + w)
                        
            return dist[-1] <= k

        low = 0
        high = max((w for _, _, w in edges), default=0)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if check(mid):
                ans = mid
                low = mid + 1 
            else:
                high = mid - 1 
                
        return ans