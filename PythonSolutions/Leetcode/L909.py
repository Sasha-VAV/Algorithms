from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        n = len(board)
        n2 = n ** 2
        dp = [-1] * (n2 + 1)
        dp[1] = 0
        i = 0
        while i < n2:
            i += 1
            if dp[i] == -1:
                continue
            new_i = i
            for j in range(i+1, min(i+7, n2 + 1)):
                a = (j - 1) // n
                b = (j - 1) % n
                if a % 2 == 1:
                    b = -b - 1
                x = board[a][b]
                if x != -1:
                    j = x
                    if x < new_i and (dp[x] > dp[new_i] + 1 or dp[x] == -1):
                        new_i = x - 1
                if dp[i] + 1 < dp[j] or dp[j] == -1: dp[j] = dp[i] + 1
            i = new_i
        return dp[-1]


if __name__ == '__main__':
    board = [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
    print(Solution().snakesAndLadders(board))