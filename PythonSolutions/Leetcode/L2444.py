from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = -1
        i = -1
        j = -1
        res = 0
        for r, num in enumerate(nums):
            if num == minK:
                i = r
            if num == maxK:
                j = r
            if not minK <= num <= maxK:
                l = r
            res += max(0, min(i, j) - l)
        return res


if __name__ == '__main__':
    print(Solution().countSubarrays([1,1,1,1],1,1))