from typing import List
from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dp = defaultdict(list)
        mod = 10 ** 9 + 7
        res = 0
        def bin_search(x, arr):
            l = 0
            r = len(arr) - 1
            rightmost = -1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < x:
                    l = mid + 1
                    rightmost = mid
                else:
                    r = mid - 1
            return rightmost

        for i, num in enumerate(nums):
            if num % 2 == 0: dp[num // 2].append(i)
        for i in range(1, len(nums) - 1):
            num = nums[i]
            curr = bin_search(i, dp[num])
            past = curr + 1
            future = len(dp[num]) - past - int(num == 0)
            res += (future % mod) * (past % mod)
            res %= mod
        return res


if __name__ == '__main__':
    arr = [6,3,6]
    print(Solution().specialTriplets(arr))