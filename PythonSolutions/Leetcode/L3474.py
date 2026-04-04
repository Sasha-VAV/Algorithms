class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        res = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        for i, c in enumerate(str1):
            if c == "T":
                for j, c2 in enumerate(str2):
                    if fixed[i+j] and res[i+j] != c2: 
                        return ""
                    res[i+j] = c2
                    fixed[i+j] = True

        for i, c in enumerate(str1):
            if c == "F":
                if any(res[i+j] != str2[j] for j in range(m)):
                    continue
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        res[j] = "b"
                        break
                else:
                    return ""
        return "".join(res)