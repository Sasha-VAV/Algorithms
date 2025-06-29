from functools import lru_cache
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = 0
        res = 0
        mod = 10 ** 9 + 7
        @lru_cache(maxsize=None)
        def pow(x, c):
            if c == 0:
                return 1
            if c % 2 == 0:
                return (pow(x, c // 2) ** 2) % mod
            return (x * pow(x, c - 1)) % mod
        for i, x in enumerate(nums):
            j = max(j, i)
            while j < len(nums) - 1 and x + nums[j+1] <= target:
                j += 1
            else:
                while j > i and x + nums[j] > target:
                    j -= 1
                if i == j and x + nums[j] > target:
                    break
            if x + nums[j] <= target:
                res += pow(2, j - i)
            res %= mod
        return res


if __name__ == '__main__':
    nums = [2,3,3,4,6,7]
    target = 12
    print(Solution().numSubseq(nums, target))