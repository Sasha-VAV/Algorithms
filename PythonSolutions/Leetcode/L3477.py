class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = len(fruits)
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets.pop(i)
                    res -= 1
                    break
        return res