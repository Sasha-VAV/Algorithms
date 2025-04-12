from typing import List
from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def fill_board(i, mask):
            if i == len(mask):
                return [mask]
            masks = []
            for j, val in enumerate(mask[i]):
                if val != 1:
                    continue
                new_mask = deepcopy(mask)
                for n_i in range(i+1, len(mask)):
                    for n_j in range(len(mask[n_i])):
                        if i == n_i or j == n_j or abs(n_i - i) == abs(n_j - j):
                            new_mask[n_i][n_j] = 0
                new_mask[i][j] = -1
                new_mask = fill_board(i+1, new_mask)
                masks.extend(new_mask)
            return masks
        mask = []
        for i in range(n):
            mask.append([1]*n)
        masks = fill_board(0, mask)
        for mask in masks:
            board = []
            for row in mask:
                board.append("".join(["Q" if x == -1 else "." for x in row]))
            res.append(board)
        return res


if __name__ == '__main__':
    print(Solution().solveNQueens(4))