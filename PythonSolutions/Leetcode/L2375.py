class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def safe_index(arr, x):
            try:
                return arr.index(x)
            except:
                return -1
        def dfs(i, prev):
            if i == len(pattern):
                return "".join([str(x) for x in prev])
            if not prev:
                for j in range(1, 10):
                    if safe_index(prev, j) != -1: continue
                    s = dfs(i, prev + [j])
                    if s: return s
                return ""
            if pattern[i] == "I":
                for j in range(prev[-1]+1, 10):
                    if safe_index(prev, j) != -1: continue
                    s = dfs(i+1, prev + [j])
                    if s: return s
                return ""
            for j in range(1, prev[-1]):
                if safe_index(prev, j) != -1: continue
                s = dfs(i+1, prev + [j])
                if s: return s
            return ""
        return dfs(0, [])