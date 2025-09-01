from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for a, b in classes:
            heapq.heappush(heap, (-(a + 1) / (b + 1) + a / b, a, b))
        while extraStudents:
            _, a, b = heapq.heappop(heap)
            a += 1
            b += 1
            extraStudents -= 1
            heapq.heappush(heap, (-(a + 1) / (b + 1) + a / b, a, b))
        res = 0
        for _, a, b in heap:
            res += a / b
        return res / len(classes)


if __name__ == '__main__':
    classes = [[1,2],[3,5],[2,2]]
    extraStudents = 2
    print(Solution().maxAverageRatio(classes, extraStudents))