class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        heap = [(-health, 0, 0)]
        n = len(grid)
        m = len(grid[0])

        best_healths = defaultdict(int)
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while heap:
            health, i, j = heapq.heappop(heap)
            health *= -1
            if health - grid[i][j] < 1 or health < best_healths[(i, j)]:
                continue
            if i == n - 1 and j == m - 1:
                return True
            
            health -= grid[i][j]
            
            for i_shift, j_shift in shifts:
                i_new, j_new = i + i_shift, j + j_shift
                if not 0 <= i_new < n or not 0 <= j_new < m:
                    continue
                if health > best_healths[(i_new, j_new)]:
                    best_healths[(i_new, j_new)] = health
                    heap.append((-health, i_new, j_new))
        return False