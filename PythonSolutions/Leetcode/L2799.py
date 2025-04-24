from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        right = 0
        res = 0
        unique_nums = set(nums)
        curr_nums = dict()
        n = len(nums)
        for l in range(n):
            while curr_nums.keys() != unique_nums:
                if right == n:
                    return res
                curr_nums[nums[right]] = curr_nums.get(nums[right], 0) + 1
                right += 1
            if curr_nums.keys() == unique_nums:
                res += n - right + 1
            if curr_nums[nums[l]] == 1:
                curr_nums.pop(nums[l])
            else:
                curr_nums[nums[l]] -= 1
        return res


if __name__ == '__main__':
    print(Solution().countCompleteSubarrays([1, 3, 1, 2, 2]))