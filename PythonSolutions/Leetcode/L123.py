from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        changes = [0]
        for i, price in enumerate(prices[1:]):
            if prices[i] * price < 0:
                changes.append(i)
        changes.append(len(prices)-1)
        def find_max_seq_sum(l, r):
            if l >= len(prices):
                return 0, -1
            best_sum = prices[l]
            curr_sum = 0
            idx = l
            max_idx = l
            for i in range(l, r):
                if prices[i] >= curr_sum + prices[i]:
                    curr_sum = prices[i]
                    idx = i
                else:
                    curr_sum += prices[i]
                if curr_sum > best_sum:
                    max_idx = idx
                    best_sum = curr_sum
            return best_sum, max_idx
        n = len(prices)
        right_sum, right_idx = find_max_seq_sum(0, n)
        max_profit = right_sum
        left_best = 0
        left_curr = 0
        for i in range(n):
            left_curr = max(left_curr + prices[i], prices[i])
            left_best = max(left_best, left_curr)
            if i >= right_idx:
                if i in changes:
                    right_sum, right_idx = find_max_seq_sum(i+1, n)
                else:
                    right_sum = 0
            max_profit = max(max_profit, right_sum + left_best, right_sum, left_best)
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5]))