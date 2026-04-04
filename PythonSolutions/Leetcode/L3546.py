from typing import List


class Solution:
    def _horizontal_partition(self, grid: list[list[int]]) -> bool:
        sum_arr = [sum(row) for row in grid]
        all_sum = sum(sum_arr)
        if all_sum % 2 == 1: return False

        curr = 0
        for row_sum in sum_arr:
            curr += row_sum
            diff = all_sum - curr
            if diff == curr:
                return True
            elif diff < curr:
                return False
        raise NotImplementedError("Should be unreachable")

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        return self._horizontal_partition(grid) or self._horizontal_partition(list(zip(*grid[::-1])))


if __name__ == "__main__":
    arr = [[1,4], [2,3]]
    print(Solution().canPartitionGrid(arr))