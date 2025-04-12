from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        def backtrack(nums, target, alphabet):
            nonlocal combinations
            if sum(nums) >= target:
                if sum(nums) == target:
                    combinations.append(nums)
                return
            for i, letter in enumerate(alphabet):
                backtrack(nums + [letter], target, alphabet[i:])
            return
        backtrack([], target, nums)
        return combinations


if __name__ == '__main__':
    nums = [3, 4, 5]
    target = 16
    print(Solution().combinationSum(nums, target))