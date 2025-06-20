class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        north = south = east = west = 0
        for i, c in enumerate(s):
            match c:
                case "N":
                    north += 1
                case "S":
                    south += 1
                case "E":
                    east += 1
                case "W":
                    west += 1
            x, y = abs(north - south), abs(west - east)
            md = x + y
            distance = md + min(2 * k, i + 1 - md)
            res = max(res, distance)
        return res

