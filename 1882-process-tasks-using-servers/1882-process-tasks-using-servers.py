import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        unavailable = []
        ans = []
        current_time = 0
        
        for j, task in enumerate(tasks):
            current_time = max(current_time, j)
            
            if not available and unavailable[0][0] > current_time:
                current_time = unavailable[0][0]
            
            while unavailable and unavailable[0][0] <= current_time:
                _, w, i = heapq.heappop(unavailable)
                heapq.heappush(available, (w, i))
            
            w, i = heapq.heappop(available)
            ans.append(i)
            heapq.heappush(unavailable, (current_time + task, w, i))
            
        return ans