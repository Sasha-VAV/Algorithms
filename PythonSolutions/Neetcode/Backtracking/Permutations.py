from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(chosen: list):
            if len(chosen) == len(nums):
                return [chosen]
            res = []
            for num in nums:
                if num in chosen:
                    continue
                res.extend(permute(chosen + [num]))
            return res
        return permute([])


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))