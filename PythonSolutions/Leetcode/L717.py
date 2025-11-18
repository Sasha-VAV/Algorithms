from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1: return True
        dp = [False] * len(bits)
        for i in range(len(bits) - 1):
            if bits[i] == 0 and (i == 0 or dp[i - 1]):
                dp[i] = True
                continue
            if bits[i] == 1 and (i == 0 or dp[i - 1]):
                dp[i+1] = True
        return dp[-2]


if __name__ == '__main__':
    arr = [1,1,1,0]
    print(Solution().isOneBitCharacter(arr))