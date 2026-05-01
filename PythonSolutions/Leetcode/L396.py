class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = 0
        arr_sum = 0
        for i, x in enumerate(nums):
            arr_sum += x
            res += i * x
        n = len(nums)
        curr = res
        for k in range(n - 1):
            curr -= arr_sum
            curr += n * nums[k]
            res = max(res, curr)
        return res