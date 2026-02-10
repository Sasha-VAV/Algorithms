from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if len(nums) - i <= res: return res
            used = set()
            balance = 0
            for j in range(i, len(nums)):
                if nums[j] not in used:
                    if nums[j] % 2 == 0:
                        balance += 1
                    else:
                        balance -= 1
                    used.add(nums[j])
                if balance == 0:
                    res = max(res, j - i + 1)
        return res