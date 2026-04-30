class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[] for _ in range(m)]
        def get_score_cost(x):
            match x:
                case 0:
                    return 0, 0
                case 1:
                    return 1, 1
                case 2:
                    return 2, 1
            raise ValueError(f"Wrong value {x}")
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                curr = []
                if j > 0:
                    curr.extend(dp[j - 1])
                if i > 0:
                    curr.extend(dp[j])
                if i == 0 and j == 0:
                    curr.append((0, 0))
                if not curr:
                    dp[j] = []
                    continue
                
                heapq.heapify(curr)
                curr_cost = curr[0][1] + 1
                tmp = []
                x_score, x_cost = get_score_cost(x)
                while curr:
                    score, cost = heapq.heappop(curr)
                    if cost >= curr_cost or x_cost + cost > k:
                        continue
                    curr_cost = cost
                    tmp.append((score - x_score, cost + x_cost))
                dp[j] = tmp
        return -1 if not dp[j] else -dp[j][0][0]