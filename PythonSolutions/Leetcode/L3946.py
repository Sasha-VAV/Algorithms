DIVISORS = [(0,)]
for i in range(1, 1501):
    divs = []
    for j in range(1, i + 1):
        if i % j == 0:
            divs.append(j)
    DIVISORS.append(tuple(divs))

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        free_copies = defaultdict(int)
        for factor, _ in items:
            for divisor in DIVISORS[factor]:
                free_copies[divisor] += 1
        heap = []
        cheapest_item = min(price for _, price in items)
        best_amount = [0] * (budget + 1)
        for i in range(0, budget + 1, cheapest_item):
            best_amount[i] = i // cheapest_item

        for factor, price in items:
            quantity = free_copies[factor]
            old_amounts = best_amount.copy()
            for amount in range(price, budget + 1):
                best_amount[amount] = max(best_amount[amount], old_amounts[amount - price] + quantity)
        return max(best_amount)