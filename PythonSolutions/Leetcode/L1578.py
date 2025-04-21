from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        rm = 0
        s = ""
        for c, t in zip(colors, neededTime):
            if c != s:
                res -= rm
                s = c
                rm = 0
            res += t
            rm = max(rm, t)
        res -= rm
        return res


if __name__ == "__main__":
    print(Solution().minCost(colors="abaac", neededTime=[1,2,3,4,5]))