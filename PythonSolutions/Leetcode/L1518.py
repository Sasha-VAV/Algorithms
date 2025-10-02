class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numBottles // numExchange * numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return res + numBottles