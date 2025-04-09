from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        if min_num < k:
            return -1
        unique_nums = set(nums)
        if min_num == k:
            return len(unique_nums) - 1
        return len(unique_nums)


if __name__ == '__main__':
    nums = [2, 2, 3, 3, 5]
    k = 1
    print(Solution().minOperations(nums, k))
