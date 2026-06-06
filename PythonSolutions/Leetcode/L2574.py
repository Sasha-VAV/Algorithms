class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * (n + 1)
        right_sum = [0] * (n + 1)

        for i in range(n):
            left_sum[i + 1] = left_sum[i] + nums[i]
            right_sum[-i - 2] = right_sum[-i - 1] + nums[-i - 1]
        res = [0] * n
        for i in range(n):
            res[i] = abs(left_sum[i] - right_sum[i + 1])
        return res
