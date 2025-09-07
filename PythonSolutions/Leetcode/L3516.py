class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        r = abs(y - z) - abs(x - z)
        if r > 0: return 1
        if r < 0: return 2
        return 0