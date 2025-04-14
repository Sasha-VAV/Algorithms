class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = [0]*101
        for num in nums:
            seen[num] += 1
        res = 0
        for idx, x in enumerate(seen):
            if x == 1:
                res += idx
        return res