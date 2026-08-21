class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), val in zip(equations, values):
            graph.setdefault(a, {})[b] = val
            graph.setdefault(b, {})[a] = 1 / val

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for nxt, weight in graph[src].items():
                if nxt not in visited:
                    result = dfs(nxt, dst, visited)
                    if result != -1.0:
                        return weight * result

            return -1.0
            

        return [dfs(a, b, set()) for a, b in queries]