from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        n = len(nums)
        l = 0
        r = 0
        for i, x in enumerate(nums):
            if x == key:
                l = max(r, i - k)
                r = min(n, i + k + 1)
                for j in range(l, r):
                    res.append(j)
        return res


if __name__ == "__main__":
    nums = [3, 4, 9, 1, 3, 9, 5]
    key = 9
    k = 1
    print(Solution().findKDistantIndices(nums, key, k))