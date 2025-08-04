from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        choices = defaultdict(int)
        i = 0
        for j, v in enumerate(fruits):
            if v not in choices:
                res = max(res, j - i)
                while len(choices) == 2:
                    choices[fruits[i]] -= 1
                    if choices[fruits[i]] == 0: choices.pop(fruits[i])
                    i += 1
            choices[v] += 1
        return max(res, len(fruits) - i)


if __name__ == '__main__':
    fruits = [1,0,1,4,1,4,1,2,3]
    print(Solution().totalFruit(fruits))