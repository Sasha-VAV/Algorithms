from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while numbers[i] < (target // 2 + 1):
            while numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            i += 1


if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))
