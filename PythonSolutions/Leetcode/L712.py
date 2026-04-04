class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[None] * (1 + len(s2)) for _ in range(1 + len(s1))]
        dp[0][0] = 0
        for i in range(1 + len(s1)):
            for j in range(1 + len(s2)):
                if i == 0 or j == 0:
                    if i == 0 and j == 0:
                        continue
                    if i == 0:
                        dp[i][j] = dp[i][j - 1] + ord(s2[j-1])
                        continue
                    if j == 0:
                        dp[i][j] = dp[i - 1][j] + ord(s1[i-1])
                    continue
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "sea"
    s2 = "eat"
    print(Solution().minimumDeleteSum(s1, s2))