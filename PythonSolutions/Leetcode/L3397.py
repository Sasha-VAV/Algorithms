from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = nums[0] - k
        res = 1
        for num in nums[1:]:
            if num + k <= prev: continue
            prev = max(num - k, prev + 1)
            res += 1
        return res


if __name__ == '__main__':
    arr = [4,4,4,4]
    print(Solution().maxDistinctElements(arr, 1))