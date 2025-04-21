from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_low = 0
        max_up = 0
        val = 0
        for diff in differences:
            val += diff
            min_low = min(min_low, val)
            max_up = max(max_up, val)
        res = upper - lower - max_up + min_low + 1
        return res if res > 0 else 0


if __name__ == '__main__':
    print(Solution().numberOfArrays(differences=[-65222,8035,18772,88538,38372,-20575,-34385,19665], lower=-72503, upper=84339))
