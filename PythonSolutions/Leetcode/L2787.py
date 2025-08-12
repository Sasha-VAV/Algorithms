class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        a = 1
        mod = 10 ** 9 + 7
        while (v := pow(a, x)) <= n:
            for i in range(n, v - 1, -1):
                dp[i] = (dp[i] + dp[i - v]) % mod
            a += 1
        return dp[-1]

