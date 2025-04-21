from collections import Counter
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        avg = sum(nums) / n
        cache = dict()
        def possible_sum(arr, target, max_nums, idx):
            if (target, max_nums, idx) in cache:
                return cache[(target, max_nums, idx)]
            if max_nums < 0 or target < 0:
                cache[(target, max_nums, idx)] = False
                return False
            if idx == len(arr):
                if max_nums == 0 and target == 0:
                    cache[(target, max_nums, idx)] = True
                    return True
                cache[(target, max_nums, idx)] = False
                return False
            x = arr[idx]
            ans = possible_sum(arr, target-x, max_nums-1, idx+1) or possible_sum(arr, target, max_nums, idx+1)
            cache[(target, max_nums, idx)] = ans
            return ans

        for i in range(1, n//2+1):
            target = avg * i
            if abs(round(target) - target) > 1e-6:
                continue
            target = int(target)
            if possible_sum(nums, target, i, 0):
                return True
        return False


if __name__ == '__main__':
    print(Solution().splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))