class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(i):
            nonlocal visited
            if not (0 <= i < len(arr)) or i in visited:
                return False
            visited.add(i)
            if arr[i] == 0:
                return True
            return dfs(i - arr[i]) or dfs(i + arr[i])
        return dfs(start)