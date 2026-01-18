from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix_x = [[0] * (n + 1) for _ in range(m)]
        prefix_y = [[0] * (n) for _ in range(m + 1)]
        prefix_diag_up_left = {}
        prefix_diag_up_right = {}
        # fill prefixes
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                prefix_x[i][j+1] = prefix_x[i][j] + curr
                prefix_y[i+1][j] = prefix_y[i][j] + curr
                x, y = j, i
                shift = min(x, y)
                x -= shift
                y -= shift
                if (x, y) not in prefix_diag_up_left:
                    prefix_diag_up_left[(x, y)] = [0]
                prefix_diag_up_left[(x, y)].append(prefix_diag_up_left[(x, y)][-1] + curr)
                x, y = j, i
                shift = min(n - x - 1, y)
                x += shift
                y -= shift
                if (x, y) not in prefix_diag_up_right:
                    prefix_diag_up_right[(x, y)] = [0]
                prefix_diag_up_right[(x, y)].append(prefix_diag_up_right[(x, y)][-1] + curr)

        def square_exist(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if k == 3 and i == 1 and j == 1:
                        pass
                    curr = None
                    for shift in range(k):
                        curr_row = prefix_x[i+shift][j+k] - prefix_x[i+shift][j]
                        curr_col = prefix_y[i+k][j+shift] - prefix_y[i][j+shift]
                        if curr is None: curr = curr_row
                        if curr_row != curr: break
                        if curr_col != curr: break
                    else:
                        x, y = j, i
                        shift = min(x, y)
                        x -= shift
                        y -= shift
                        curr_diag = prefix_diag_up_left[(x, y)][shift + k] - prefix_diag_up_left[(x, y)][shift]
                        if curr_diag != curr:
                            continue
                        x, y = j + k - 1, i
                        shift = min(n - x - 1, y)
                        x += shift
                        y -= shift
                        curr_diag = prefix_diag_up_right[(x, y)][shift + k] - prefix_diag_up_right[(x, y)][shift]
                        if curr_diag != curr:
                            continue
                        return True
            return False

        for k in range(min(n, m), 0, -1):
            if square_exist(k):
                return k
        raise NotImplementedError


if __name__ == "__main__":
    arr = [[1]]
    print(Solution().largestMagicSquare(arr))