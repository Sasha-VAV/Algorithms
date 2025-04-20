from typing import List
import math
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        numbers = Counter(answers)
        res = 0
        for k, v in numbers.items():
            res += math.ceil(v/(k+1)) * (k+1)
        return res


if __name__ == '__main__':
    print(Solution().numRabbits([1, 1, 1]))