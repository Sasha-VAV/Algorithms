class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 <= costBoth:
            return need1 * cost1 + need2 * cost2
        if need1 > need2:
            return costBoth * need2 + min(costBoth, cost1) * (need1 - need2)
        return costBoth * need1 + min(costBoth, cost2) * (need2 - need1)