from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diffs = [0] * (len(nums) + 1)
        for a, b in queries:
            diffs[a] += 1
            diffs[b+1] -= 1
        for i in range(len(nums)):
            if i < len(nums) - 1:
                diffs[i+1] += diffs[i]
            if diffs[i] < nums[i]:
                return False
        return True


if __name__ == '__main__':
    nums = [1, 0, 1]
    queries = [[0, 2]]
    print(Solution().isZeroArray(nums, queries))