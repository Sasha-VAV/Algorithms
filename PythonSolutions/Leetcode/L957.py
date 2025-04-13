from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        days = []
        for day in range(n):
            new_cells = cells.copy()
            if new_cells in days:
                idx = days.index(new_cells)
                loop_len = day - idx
                new_idx = (n - day) % loop_len + idx
                return days[new_idx]
            for i in range(len(cells)):
                if i == 0 or i == len(cells) - 1:
                    new_cells[i] = 0
                    continue
                new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
            days.append(new_cells)
            cells = new_cells
        return cells


if __name__ == '__main__':
    cells = [1, 0, 0, 1, 0, 0, 1, 0]
    n = 1000000000
    print(Solution().prisonAfterNDays(cells, n))