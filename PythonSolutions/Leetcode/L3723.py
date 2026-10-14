class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1:
            return ""
        res = []
        nines, rest = divmod(sum, 9)
        if nines + bool(rest) > num:
            return ""
        res = ["9"] * nines
        if rest:
            res.append(str(rest))
        res.extend(["0"] * (num - len(res)))
        return "".join(res)