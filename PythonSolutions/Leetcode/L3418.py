class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        max_n = 2

        max_n += 1
        dp = [[[float('-inf')] * max_n for _ in range(2)] for _ in range(len(coins[0]))]
        dp[0][0][0] = 0
        for row in coins:
            for j, x in enumerate(row):
                for i in range(max_n):
                    dp[j][1][i] = max(dp[j][0][i], (dp[j-1][0][i] if j > 0 else float('-inf')))
                    dp[j][0][i] = max(dp[j][1][i] + x, (dp[j][1][i-1] if i > 0 else float('-inf')))
        return max(dp[-1][0])


if __name__ == "__main__":
    grid = [[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]]
    print(Solution().maximumAmount(grid))