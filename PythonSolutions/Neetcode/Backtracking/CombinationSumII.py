from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtrack(nums, target, alphabet):
            nonlocal combinations
            if sum(nums) >= target:
                if sum(nums) == target and nums not in combinations:
                    combinations.append(nums)
                return
            for i, letter in enumerate(alphabet):
                backtrack(nums + [letter], target, alphabet[i+1:])
            return

        backtrack([], target, candidates)
        return combinations


if __name__ == '__main__':
    candidates = [9,2,2,4,6,1,5]
    target = 8
    print(Solution().combinationSum2(candidates, target))