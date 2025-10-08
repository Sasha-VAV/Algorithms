from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        needed = sorted([success / potion for potion in potions])
        dp = [0] * (max(spells) + 1)
        eps = 1e-9
        j = 0
        for i in range(1, len(dp)):
            while j < len(needed) and needed[j] < i + eps:
                j += 1
            dp[i] = j
        return [dp[x] for x in spells]


if __name__ == '__main__':
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    print(Solution().successfulPairs(spells, potions, success))
