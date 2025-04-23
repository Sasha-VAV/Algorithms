from typing import List


class Solution:
    def maxProfit(self, k, prices: List[int]) -> int:
        buy = prices[0]
        possible_trades = []
        n = len(prices)
        for _, price in enumerate(prices[1:]):
            i = _ + 1
            if price < buy:
                buy = price
            if i == n - 1 or price > prices[i + 1]:
                if price - buy > 0:
                    possible_trades.append((price - buy, price))
                if i == n - 1:
                    continue
                buy = prices[i + 1]
        while len(possible_trades) > k:
            running_sum = sum(trade[0] for trade in possible_trades)
            max_sum = 0
            idx = 0
            new_val = possible_trades[0]
            m = len(possible_trades)
            for i, trade in enumerate(possible_trades):
                if i < m - 1:
                    curr_sum = running_sum - possible_trades[i + 1][0] + possible_trades[i + 1][1] - trade[1]
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                        idx = i
                        new_val = (trade[0] + possible_trades[i+1][1] - trade[1], possible_trades[i+1][1])
                curr_sum = running_sum - trade[0]
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    idx = i - 1
                    new_val = None
            if new_val is not None:
                possible_trades[idx] = new_val
            possible_trades.pop(idx+1)
        return sum(trade[0] for trade in possible_trades)
