class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        prev_row = [0 for _ in range(len(grid[0]))]
        has_row_x = [False for _ in range(len(prev_row))]
        res = 0
        for row in grid:
            curr = 0
            for j, x in enumerate(row):
                match x:
                    case "X":
                        x = 1
                        has_row_x[j] = True
                    case "Y":
                        x = -1
                    case _:
                        x = 0
                if not has_row_x[j] and j > 0 and has_row_x[j - 1]:
                    has_row_x[j] = True

                prev_row[j] += x
                curr += prev_row[j]
                if curr == 0 and has_row_x[j]:
                    res += 1
        return res