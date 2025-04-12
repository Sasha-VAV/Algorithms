from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def build_path(i, j, idx):
            if idx == len(word):
                return True
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[idx] or board[i][j] == '#':
                return False
            board[i][j] = "#"
            tmp = build_path(i-1, j, idx+1)
            tmp += build_path(i, j-1, idx+1)
            tmp += build_path(i+1, j, idx+1)
            tmp += build_path(i, j+1, idx+1)
            board[i][j] = word[idx]
            return tmp
        for i in range(len(board)):
            for j in range(len(board[0])):
                if build_path(i, j, 0, ):
                    return True
        return False


if __name__ == '__main__':
    board = [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"]
    ]
    word = "CAT"
    print(Solution().exist(board, word))
