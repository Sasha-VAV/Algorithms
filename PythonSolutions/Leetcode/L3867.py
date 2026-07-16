class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = [-1] * len(nums)

        curr_max = 0
        for i, num in enumerate(nums):
            curr_max = max(curr_max, num)
            prefix_gcd[i] = gcd(num, curr_max)
        
        prefix_gcd.sort()

        res = 0
        for i in range(len(prefix_gcd) // 2):
            res += gcd(prefix_gcd[i], prefix_gcd[-i - 1])
        return res