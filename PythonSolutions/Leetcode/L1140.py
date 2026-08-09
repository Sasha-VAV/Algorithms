from typing import List
from functools import cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i, pile in enumerate(reversed(piles)):
            suffix_sum[-i - 2] = pile + suffix_sum[-i - 1]

        @cache
        def dfs(idx: int, m: int):
            if idx == n:
                return 0
            
            max_gain = 0
            for i in range(idx, min(n, idx + 2 * m)):
                future_gain = dfs(i + 1, max(m, i - idx + 1))
                max_gain = max(max_gain, suffix_sum[idx] - future_gain)
            if max_gain is None:
                raise NotImplementedError
            
            return max_gain
        
        return dfs(0, 1)


if __name__ == "__main__":
    piles = [2,7,9,4,4]
    print(Solution().stoneGameII(piles=piles))