class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        curr = 0
        i = 0
        while i < len(directions) and directions[i] == "L":
            i += 1
        for d in directions[i:]:
            if d == "R":
                curr += 1
            else:
                if d == "L": curr += 1
                res += curr
                curr = 0
        return res