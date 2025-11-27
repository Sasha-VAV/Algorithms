from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix[i+1] = num + prefix[i]
        dp = [float("-inf")] * (len(nums) + 1)
        for i in range(k, len(nums) + 1):
            dp[i] = max(dp[i - k], 0)
            dp[i] += prefix[i] - prefix[i - k]
        return max(dp)


if __name__ == '__main__':
    arr = [1, 2]
    c = 1
    print(Solution().maxSubarraySum(arr, c))