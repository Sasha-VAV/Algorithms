class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        def dfs(i, j, prev_i, prev_j):
            if (i, j) in visited:
                return prev_i is not None
                        
            visited.add((i, j))

            for i_shift, j_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = i + i_shift, j + j_shift
                if new_i == prev_i and new_j == prev_j:
                    continue
                if not (0 <= new_i < n and 0 <= new_j < m):
                    continue
                if grid[i][j] != grid[new_i][new_j]:
                    continue
                if dfs(new_i, new_j, i, j):
                    return True
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, None, None):
                    return True
        return False
        