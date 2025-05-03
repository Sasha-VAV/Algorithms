class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        j = 0
        char = s[j]
        res = []
        for i, c in enumerate(s):
            if c != char:
                if i - j >= 3:
                    res.append([j, i - 1])
                j = i
                char = c
        if len(s) - j >= 3:
            res.append([j, len(s) - 1])
        return res