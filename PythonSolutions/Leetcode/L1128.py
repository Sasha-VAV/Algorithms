from typing import List
from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        nums = Counter()
        res = 0
        for domino in dominoes:
            domino.sort()
            nums.update((tuple(domino),))
        for v in nums.values():
            res += (v - 1) * v // 2
        return res


if __name__ == '__main__':
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    print(Solution().numEquivDominoPairs(dominoes))
