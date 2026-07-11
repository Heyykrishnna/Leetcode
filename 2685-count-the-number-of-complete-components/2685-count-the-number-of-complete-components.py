class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    a, b = dfs(nei)
                    nodes += a
                    degree += b

            return nodes, degree

        for i in range(n):
            if not visited[i]:
                nodes, degree = dfs(i)
                edges = degree // 2

                if edges == nodes * (nodes - 1) // 2:
                    answer += 1

        return answer