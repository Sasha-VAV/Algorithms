from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        local_max = prices[0]
        local_min = prices[0]
        for price in prices:
            if price < local_min:
                local_min = price
                local_max = price
            if price > local_max:
                local_max = price
                max_profit = max(max_profit, local_max - local_min)
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
