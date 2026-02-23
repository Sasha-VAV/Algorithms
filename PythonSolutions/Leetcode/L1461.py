class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = set()
        for i in range(len(s) - k + 1):
            num = s[i:i+k]
            res.add(num)
        return len(res) == 2 ** k