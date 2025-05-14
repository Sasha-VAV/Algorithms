from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if x2 == x1:
                    k = float('inf')
                    b = x2
                else:
                    k = (y2-y1) / (x2 - x1)
                    b = y2 - k * x2
                lines[(k, b)].add((x1, y1))
                lines[(k, b)].add((x2, y2))
        if len(points) < 2:
            return 1
        return max(map(len, lines.values()))


if __name__ == '__main__':
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(Solution().maxPoints(points))