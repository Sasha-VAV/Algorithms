class Solution:
    def canAliceWin(self, n: int) -> bool:
        # i can derive the formula, but that's not a good solution for given constraints
        for i, x in enumerate(range(10, -1, -1)):
            n -= x
            if n < 0:
                return i % 2 == 1
        raise ValueError