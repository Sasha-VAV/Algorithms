from typing import List
from collections import deque
import heapq

DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

class Solution:
    def maximumSafenessFactor(self, dp: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            value = dp[i][j]

            for i_shift, j_shift in DIRECTIONS:
                x = i_shift + i
                y = j_shift + j
                if 0 <= x < n and 0 <= y < n and not dp[x][y]:
                    dp[x][y] = value + 1
                    q.append((x, y))
        
        heap = [(-dp[0][0], 0, 0)]
        dp[0][0] = None
        while heap:
            value, i, j = heapq.heappop(heap)
            if i == n - 1 and j == n - 1:
                return -value - 1
            
            for i_shift, j_shift in DIRECTIONS:
                x = i + i_shift
                y = j + j_shift

                if 0 <= x < n and 0 <= y < n and dp[x][y] is not None:
                    heapq.heappush(heap, (-min(-value, dp[x][y]), x, y))
                    dp[x][y] = None
            
        
        raise NotImplementedError
    
if __name__ == "__main__":
    grid = [[1,1,0],[1,1,0],[1,1,0]]
    print(Solution().maximumSafenessFactor(grid))