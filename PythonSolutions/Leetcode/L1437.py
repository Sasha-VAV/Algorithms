from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k - 1
        for i, num in enumerate(nums):
            if num != 1: continue
            if i - prev <= k: return False
            prev = i
        return True


if __name__ == '__main__':
    arr = [1,0,0,0,1,0,0,1]
    print(Solution().kLengthApart(arr, 2))