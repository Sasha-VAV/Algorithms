class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(map(int, str(x)))
        for i, num in enumerate(nums):
            if digit_sum(num) == i:
                return i
        