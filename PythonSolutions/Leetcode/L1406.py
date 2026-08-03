class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            best = float('-inf')
            curr = 0

            for k in range(1, 4):
                if i + k > n:
                    continue
                
                curr += stones[i + k - 1]
                best = max(best, curr - dp[i + k])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

