class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        for i, cost in enumerate(sorted(costs)):
            if cost > coins:
                return i
            coins -= cost
        return len(costs)