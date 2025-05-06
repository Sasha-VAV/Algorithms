from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ops = dict()
        for (a, b), val in zip(equations, values):
            ops[a] = ops.get(a, []) + [(b, val)]
            ops[b] = ops.get(b, []) + [(a, 1/val)]
        cache = dict()
        res = []
        for a, b in queries:
            seen = set()
            if b not in ops:
                res.append(-1)
                continue
            def search(i):
                if (i, b) in cache:
                    return cache[(i, b)]
                if i in seen or i not in ops:
                    return -1
                if i == b:
                    return 1
                seen.add(i)
                for c, x in ops[i]:
                    value = search(c)
                    if value != -1:
                        cache[(i, b)] = value * x
                        return value * x
                return -1
            res.append(search(a))
        return res


if __name__ == '__main__':
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(Solution().calcEquation(equations, values, queries))