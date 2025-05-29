from functools import lru_cache
from typing import List
from collections import defaultdict


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        tree1 = defaultdict(set)
        tree2 = defaultdict(set)
        for a, b in edges1:
            tree1[a].add(b)
            tree1[b].add(a)
        for a, b in edges2:
            tree2[a].add(b)
            tree2[b].add(a)
        @lru_cache(maxsize=None)
        def dfs(node, prev, mode):
            children = tree1[node] if mode == 1 else tree2[node]
            even = 1
            odd = 0
            for child in children:
                if child == prev:
                    continue
                child_even, child_odd = dfs(child, node, mode)
                even += child_odd
                odd += child_even
            return even, odd

        max_tree2 = dfs(0, None, 2)
        max_tree2 = max(max_tree2[0], max_tree2[1])
        res = [-1] * len(tree1)
        tree1_even, tree1_odd = dfs(0, None, 1)
        del dfs
        def dfs(node, prev, even, odd):
            if res[node] != -1:
                return
            res[node] = even
            for child in tree1[node]:
                if child == prev:
                    continue
                dfs(child, node, odd, even)
        dfs(0, None, tree1_even, tree1_odd)
        res = [x + max_tree2 for x in res]
        return res

if __name__ == '__main__':
    edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
    print(Solution().maxTargetNodes(edges1, edges2))
