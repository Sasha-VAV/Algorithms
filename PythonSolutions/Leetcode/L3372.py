from functools import lru_cache
from typing import List
from collections import defaultdict


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree1 = defaultdict(set)
        tree2 = defaultdict(set)
        for a, b in edges1:
            tree1[a].add(b)
            tree1[b].add(a)
        for a, b in edges2:
            tree2[a].add(b)
            tree2[b].add(a)
        @lru_cache(maxsize=1024)
        def dfs(node, count, prev=None, mode=1):
            if mode == 1:
                tree = tree1
            else:
                tree = tree2
            if count > k:
                return 0
            if count == k:
                return 1
            res = 1
            for neighbor in tree[node]:
                if neighbor == prev:
                    continue
                res += dfs(neighbor, count + 1, node, mode)
            return res
        max_tree2 = 0
        for key in tree2:
            max_tree2 = max(max_tree2, dfs(key, 1, None, 2))
        ans = [0] * len(tree1)
        for i in range(len(tree1)):
            ans[i] = dfs(i, 0, None, 1) + max_tree2
        return ans


if __name__ == '__main__':
    edges1 = [[0, 1]]
    edges2 = [[0, 1]]
    k = 0
    print(Solution().maxTargetNodes(edges1, edges2, k))
