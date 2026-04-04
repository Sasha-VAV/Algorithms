class Solution:
    def binaryGap(self, n: int) -> int:
        last_pos = 1000
        res = 0
        i = 0
        while n > 0:
            curr = n & 1
            if curr:
                if last_pos is not None:
                    res = max(res, i - last_pos)
                last_pos = i
            n >>= 1
            i += 1
        return res