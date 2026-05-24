class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n
        
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            
            best = 1
            # left scan
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            
            # right scan
            for j in range(i + 1, i + d + 1):
                if j >= n or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))
            
            dp[i] = best
            return best
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res