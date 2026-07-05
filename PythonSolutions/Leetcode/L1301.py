from typing import List


MODULO = 10 ** 9 + 7


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # since the path from the end and the start is going to be equal
        # we're going from the end to the start
        n = len(board)
        dp = [0] * n
        counts = [0] * n

        for row in board:
            curr_dp = [0] * n
            curr_count = [0] * n
            for j, c in enumerate(row):
                if c == "E":
                    curr_count[j] = 1
                    continue
                if c == "X":
                    curr_dp[j] = 0
                    curr_count[j] = 0
                    continue
                curr = 0
                if c != "S":
                    curr = int(c)

                left = [0, 0]
                if j > 0:
                    left = [curr_dp[j - 1], curr_count[j - 1]]
                up = [dp[j], counts[j]]
                up_left = [0, 0]
                if j > 0:
                    up_left = [dp[j - 1], counts[j - 1]]
                best_score = max(left[0], up[0], up_left[0])
                count = sum(x[1] for x in (left, up, up_left) if x[0] == best_score)
                if count == 0:
                    best_score = 0
                else:
                    best_score += curr

                curr_dp[j] = best_score
                curr_count[j] = count % MODULO
            dp = curr_dp
            counts = curr_count
        return [dp[-1], counts[-1]]


if __name__ == "__main__":
    board = ["E12","1X1","21S"]
    print(Solution().pathsWithMaxScore(board))