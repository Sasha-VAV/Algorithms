MAX = 10 ** 5 + 1
dp = [False] * MAX

squares = []
curr = 1
while curr < sqrt(MAX):
    squares.append(curr ** 2)
    curr += 1

for i in range(MAX):
    if dp[i]:
        continue
    
    for square in squares:
        if square + i >= MAX:
            break
        dp[square + i] = True


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dp[n]
