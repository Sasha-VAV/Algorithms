from typing import List
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        ref = [float('inf')] * n * m
        
        heap = [(grid[0][0], 0, 0)]
        ref[0] = grid[0][0]

        while heap:
            cost, i, j = heapq.heappop(heap)
            if cost > ref[i * m + j]:
                continue
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + ii, j + jj
                if 0 <= x < n and 0 <= y < m and ref[x * m + y] > (curr := max(cost, grid[x][y])):
                    ref[x * m + y] = curr
                    heapq.heappush(heap, (curr, x, y))
        
        sorted_queries = iter(sorted(queries))
        curr = next(sorted_queries)
        res = {curr: 0}
        ref.append(float('inf')) # to avoid after loop check
        for cost in sorted(ref):
            while curr <= cost:
                try:
                    prev = res[curr]
                    curr = next(sorted_queries)
                    res[curr] = prev
                except StopIteration:
                    break
            else:
                res[curr] += 1
                continue
            break

        return [res[x] for x in queries]


if __name__ == "__main__":
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5,6,2]
    print(Solution().maxPoints(grid, queries))