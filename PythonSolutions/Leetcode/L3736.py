class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum_nums = 0
        max_num = 0
        for num in nums:
            max_num = max(max_num, num)
            sum_nums += num
        return max_num * len(nums) - sum_nums