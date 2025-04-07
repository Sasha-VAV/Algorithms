from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        max_diff = 0
        max_i = 0
        for k in range(len(nums)):
            max_val = max(max_val, max_diff * nums[k])
            max_diff = max(max_diff, max_i - nums[k])
            max_i = max(max_i, nums[k])
        return max_val


if __name__ == "__main__":
    arr = [12,6,1,2,7]
    print(Solution().maximumTripletValue(arr))