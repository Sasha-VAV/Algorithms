class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        res = [0] * value
        for num in nums:
            res[num % value] += 1

        i = 0
        while res[i % value]:
            res[i % value] -= 1
            i += 1
        return i