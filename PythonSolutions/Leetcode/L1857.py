from collections import defaultdict, Counter
from functools import lru_cache
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        unvisited_nodes = set()
        nodes = []
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            unvisited_nodes.add(u)
            unvisited_nodes.add(v)

        permanent_nodes = set()
        temporary_nodes = set()
        def visit(node):
            if node in permanent_nodes:
                return 0
            if node in temporary_nodes:
                return -1
            temporary_nodes.add(node)
            for neighbor in graph[node]:
                if visit(neighbor) == -1: return -1
            permanent_nodes.add(node)
            nodes.append(node)
            return 0

        while unvisited_nodes:
            new_node = unvisited_nodes.pop()
            if visit(new_node) == -1: return -1
        del permanent_nodes, temporary_nodes, unvisited_nodes
        if len(nodes) == 0: return 1
        dp = [[0] * 26 for _ in range(len(nodes))]
        def copy_max(arr1, arr2):
            return [max(a, b) for a, b in zip(arr1, arr2)]
        for node in nodes:
            curr = [0] * 26
            for neighbor in graph[node]:
                curr = copy_max(curr, dp[neighbor])
            color = ord(colors[node]) - ord('a')
            curr[color] += 1
            dp[node] = curr
        res = -1
        for node in dp:
            res = max(res, max(node))
        return res

if __name__ == '__main__':
    colors = "a"
    edges = []
    print(Solution().largestPathValue(colors, edges))