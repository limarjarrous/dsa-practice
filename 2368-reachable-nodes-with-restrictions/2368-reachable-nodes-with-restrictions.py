class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        visited = set(restricted)
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            size = 1
            visited.add(node)
            for nxt in graph[node]:
                if nxt not in visited:
                    size += dfs(nxt)
            return size


        return 0 if 0 in visited else dfs(0)