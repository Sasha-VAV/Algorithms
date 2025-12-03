from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # 3 hours and memory limit...
        unique_lines = defaultdict(dict) #int)
        def get_max_point(point1, point2):
            point1 = tuple(point1)
            point2 = tuple(point2)
            return frozenset({point1, point2})
        def get_line(point1, point2):
            if point1[0] == point2[0]:
                k = "inf"
                b = point1[0]
            else:
                k = (point2[1] - point1[1]) / (point2[0] - point1[0])
                b = point1[1] - k * point1[0]
                k = round(k, 7)
                b = round(b, 7)
            return k, b

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                k, b = get_line(points[i], points[j])
                if b not in unique_lines[k]:
                    unique_lines[k][b] = []
                unique_lines[k][b].append(get_max_point(points[i], points[j]))
        res = set()
        for v in unique_lines.values():
            tmp = list(v.values())
            for i in range(len(tmp) - 1):
                for j in range(i + 1, len(tmp)):
                    for x in tmp[i]:
                        for y in tmp[j]:
                            res.add(tuple(sorted([*x, *y])))
            v.clear()
        return len(res)


if __name__ == "__main__":
    arr = []
    print(Solution().countTrapezoids(arr))