class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        all_sum = sum(nums)
        if all_sum < x:
            return -1
        n = len(nums)
        res = n + 1
        i = 0
        curr = 0
        for j, val in enumerate(nums):
            curr += val
            while all_sum - curr < x:
                curr -= nums[i]
                i += 1

            if all_sum - curr == x:
                res = min(res, i + n - j - 1)
        return res if res != n + 1 else -1
