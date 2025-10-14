from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        needed = set()
        prev = None
        count = 0
        for i, num in enumerate(nums):
            if prev is None or num <= prev:
                count = 0
            count += 1
            if count >= k:
                if i in needed: return True
                needed.add(i + k)
            prev = num
        return False


if __name__ == '__main__':
    arr = [5,8,-2,-1]
    print(Solution().hasIncreasingSubarrays(arr, 2))