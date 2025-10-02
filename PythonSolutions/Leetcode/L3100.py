class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles -= numExchange
            numBottles += 1
            numExchange += 1
        return res + numBottles
