class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                x = board[i][j]
                if x == ".":
                    continue
                if x in rows[i] or x in cols[j] or x in blocks[i // 3 * 3 + j // 3]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                blocks[i//3 * 3 + j // 3].add(x)
        return True