class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                a = [points[i][0] - points[j][0], points[i][1] - points[j][1]]
                for k in range(i + 2, n):
                    b = [points[k][0] - points[j][0], points[k][1] - points[j][1]]
                    area = a[0] * b[1] - a[1] * b[0]
                    res = max(res, abs(area) / 2)
        return res