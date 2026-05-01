class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(i, j, prev_i, prev_j):
            if not (0 <= i < n and 0 <= j < m) or (i, j) in visited:
                return False
            
            road = grid[i][j]
            if prev_i is not None:
                match road:
                    case 1:
                        if not prev_i == i:
                            return False
                    case 2:
                        if not prev_j == j:
                            return False
                    case 3:
                        if not (prev_i == i and prev_j < j or prev_j == j and prev_i > i):
                            return False
                    case 4:
                        if not (prev_i == i and prev_j > j or prev_j == j and prev_i > i):
                            return False
                    case 5:
                        if not (prev_i == i and prev_j < j or prev_j == j and prev_i < i):
                            return False
                    case 6:
                        if not (prev_i == i and prev_j > j or prev_j == j and prev_i < i):
                            return False
                    
            if i == n - 1 and j == m - 1:
                return True
            
            visited.add((i, j))
            match road:
                case 1:
                    return dfs(i, j + 1, i, j) or dfs(i, j - 1, i, j)
                case 2:
                    return dfs(i - 1, j, i, j) or dfs(i + 1, j, i, j)
                case 3:
                    return dfs(i, j - 1, i, j) or dfs(i + 1, j, i, j)
                case 4:
                    return dfs(i + 1, j, i, j) or dfs(i, j + 1, i, j)
                case 5:
                    return dfs(i - 1, j, i, j) or dfs(i, j - 1, i, j)
                case 6:
                    return dfs(i - 1, j, i, j) or dfs(i, j + 1, i, j)
            raise NotImplementedError(f"Wrong road type given {road}")
        
        return dfs(0, 0, None, None)
    
