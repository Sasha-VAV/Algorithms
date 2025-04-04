from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for i, line in enumerate(board):
            for j, num in enumerate(line):
                if num == ".":
                    continue
                if num in cols[j] or num in rows[i] or num in blocks[i // 3 * 3 + j // 3]:
                    return False
                cols[j].add(num)
                rows[i].add(num)
                blocks[i // 3 * 3 + j // 3].add(num)
        return True


if __name__ == "__main__":
    board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))