class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_number = 1
        second_max = 1
        for num in nums:
            if num > max_number:
                second_max = max_number
                max_number = num
            elif num > second_max:
                second_max = num
        return (max_number - 1) * (second_max - 1)