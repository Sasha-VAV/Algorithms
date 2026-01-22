from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        start_len = len(nums)
        while len(nums) > 1:
            min_sum = nums[0] + nums[1]
            min_idx = 0
            need_del = False
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    need_del = True
                if nums[i] + nums[i - 1] < min_sum:
                    min_sum = nums[i] + nums[i-1]
                    min_idx = i - 1
            if not need_del:
                return start_len - len(nums)
            nums[min_idx] = min_sum
            nums.pop(min_idx + 1)
        return start_len - 1


if __name__ == '__main__':
    arr = [1, 2, 2]
    print(Solution().minimumPairRemoval(arr))