class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) < len(v2): v1 += ["0"] * (len(v2) - len(v1))
        if len(v2) < len(v1): v2 += ["0"] * (len(v1) - len(v2))
        for x, y in zip(v1, v2):
            x = int(x)
            y = int(y)
            if x > y: return 1
            if x < y: return -1
        return 0