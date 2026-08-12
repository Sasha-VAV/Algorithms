class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        i = 0
        res = 0
        for j, num in enumerate(nums):
            res = max(j - i, res)
            counts[num] += 1
            while counts[num] > k:
                counts[nums[i]] -= 1
                i += 1
        res = max(len(nums) - i, res)
        return res