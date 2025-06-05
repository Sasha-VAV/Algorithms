from functools import lru_cache
from collections import defaultdict, deque


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(set)
        for c1, c2 in zip(s1, s2):
            graph[c1].add(c2)
            graph[c2].add(c1)
        encoder = dict()
        visited = set()

        def dfs(c):
            visited.add(c)
            res = c
            for v in graph[c]:
                if v not in visited:
                    res = min(res, dfs(v))
            return res

        for k in set(baseStr):
            visited = set()
            encoder[k] = dfs(k)
        return "".join([encoder[k] for k in baseStr])


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(Solution().smallestEquivalentString(s1, s2, baseStr))