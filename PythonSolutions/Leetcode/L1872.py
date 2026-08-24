class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i, stone in enumerate(stones):
            prefix[i + 1] = prefix[i] + stone
        
        dp = [0] * n
        dp[-1] = prefix[-1]
        for i in range(n - 1, 1, -1):
            dp[i - 1] = max(dp[i], prefix[i] - dp[i])
        return dp[1]