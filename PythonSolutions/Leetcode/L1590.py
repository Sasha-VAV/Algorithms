from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        global_sum = sum(nums) % p
        dp = {0: -1}
        curr = 0
        res = len(nums)
        for i, num in enumerate(nums):
            curr = (curr + num) % p
            dp[curr] = i
            if (curr - global_sum) % p in dp:
                res = min(res, i - dp[(curr - global_sum) % p])
        return -1 if res >= len(nums) else res



if __name__ == "__main__":
    arr = [3,1,4,2]
    print(Solution().minSubarray(arr, 6))