class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[0] - nums[-1])
        for x, y in zip(nums[1:], nums[:-1]):
            max_diff = max(max_diff, abs(x - y))
        return max_diff