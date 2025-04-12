from heapq import heappush, heappop, heappushpop, nsmallest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            a, b = point
            heappush(heap, (a**2 + b**2, point))
        heap = nsmallest(k, heap)
        ans = []
        for point in heap:
            _, point = point
            ans.append(point)
        return ans


if __name__ == '__main__':
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    print(Solution().kClosest(points, 3))