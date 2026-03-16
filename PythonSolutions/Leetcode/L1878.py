from typing import List
import heapq


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        heap = []
        sums = set()
        n = len(grid)
        m = len(grid[0])
        max_size = (min(m, n) - 1) // 2
        def does_rhombus_exist(i, j, size):
            curr_sum = 0
            if size == 0: return grid[i][j]
            coords = set()

            for shift in range(size+1):
                x_shift = shift
                y_shift = size - shift
                for k1 in (-1, 1):
                    for k2 in (-1, 1):
                        x = i + k1 * x_shift
                        y = j + k2 * y_shift
                        if (x, y) in coords: continue
                        coords.add((x, y))
                        curr_sum += grid[x][y]

            return curr_sum

        for size in range(max_size, -1, -1):
            for i in range(size, n - size):
                for j in range(size, m - size):
                    current_sum = does_rhombus_exist(i, j, size)
                    if current_sum in sums: continue
                    sums.add(current_sum)
                    heapq.heappush(heap, current_sum)

                    if len(heap) == 4:
                        heapq.heappop(heap)
        return list(sorted(heap, reverse=True))


if __name__ == '__main__':
    grid =[[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]]
    print(Solution().getBiggestThree(grid))