class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def split(i, j):
            if j - i == 1:
                return nums[i]
            n = j - i
            left = split(i, i + n // 2)
            right = split(i + n // 2, j)
            if left == right:
                return left
            left_count = sum(1 for k in range(i, j) if nums[k] == left)
            right_count = sum(1 for k in range(i, j) if nums[k] == right)
            if left_count > right_count:
                return left
            return right
        return split(0, len(nums))