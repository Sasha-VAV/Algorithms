from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum % 2 != 0:
            return False
        target = arr_sum // 2
        arr = [0] * (target + 1)
        arr[0] = 1
        for num in nums:
            for j in range(len(arr) - 1, -1, -1):
                if arr[j] == 0:
                    continue
                if j + num > target:
                    continue
                elif j + num == target:
                    return True
                arr[j+num] = 1
        return arr[-1] != 0


if __name__ == "__main__":
    nums = [1, 2, 5]
    print(Solution().canPartition(nums))