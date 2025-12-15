class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        res = 0
        curr_num = -100
        curr = 0
        for price in prices:
            if curr_num - price == 1:
                curr += 1
            else:
                curr = 1
            res += curr
            curr_num = price
        return res