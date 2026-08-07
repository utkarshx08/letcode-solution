from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()

        def dfs(city):

            visited.add(city)
            changes = 0

            for neighbor, cost in graph[city]:

                if neighbor not in visited:
                    changes += cost
                    changes += dfs(neighbor)

            return changes

        return dfs(0)