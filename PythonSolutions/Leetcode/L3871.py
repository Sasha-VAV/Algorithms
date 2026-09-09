class Solution:
    def countCommas(self, n: int) -> int:
        # log not working because of numberical instability
        length = 0
        x = n
        while x:
            x //= 10
            length += 1
        res = 0
        curr = 9
        for i in range(length - 1):
            res += (i // 3) * curr
            curr *= 10
        res += ((length - 1) // 3) * (n - curr // 9 + 1)
        return res