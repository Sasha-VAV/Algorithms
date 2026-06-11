class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        max_depth = 0
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, prev=None):
            res = 0
            for x in graph[node]:
                if x == prev:
                    continue
                res = max(dfs(x, node) + 1, res)
            return res
        return pow(2, dfs(1) - 1, 10 ** 9 + 7)