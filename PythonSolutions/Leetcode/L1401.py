class Solution:
    def checkOverlap(self, radius: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = max(x1, min(xc, x2)) - xc
        y = max(y1, min(yc, y2)) - yc
        return x ** 2 + y ** 2 <= radius ** 2