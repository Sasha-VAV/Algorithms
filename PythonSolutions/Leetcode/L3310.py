class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        seen = [0] * n
        cache = [-1] * n
        invoked_by_k = [0] * n
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)
        
        res = []
        

        def dfs(x: int, start_k: bool):
            if cache[x] != -1:
                return cache[x]

            if seen[x]:
                return invoked_by_k[x]
            
            seen[x] = 1
            curr = 0
            
            for y in graph[x]:
                if start_k:
                    invoked_by_k[y] = 1
                    dfs(y, start_k)
                else:
                    curr += dfs(y, start_k)
                    cache[x] = curr
            return curr
        
        invoked_by_k[k] = 1
        dfs(k, True)
        if any(dfs(i, False) for i in range(n) if not invoked_by_k[i]):
            return list(range(n))
        return [i for i in range(n) if not invoked_by_k[i]]

            
