MODULO = 10 ** 9 + 7

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def dfs(nums):
            n = len(nums)
            if n < 3:
                return 1
            left_arr = [x for x in nums if x < nums[0]]
            right_arr = [x for x in nums if x > nums[0]]
            return dfs(left_arr) * dfs(right_arr) * math.comb(n - 1, len(left_arr)) % MODULO
        return (dfs(nums) - 1) % MODULO