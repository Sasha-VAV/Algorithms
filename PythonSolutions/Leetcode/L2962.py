class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        max_count = 0
        max_num = max(nums)
        j = 0
        n = len(nums)
        for i, num in enumerate(nums):
            while j < n and max_count < k:
                if nums[j] == max_num: max_count += 1
                j += 1
            if max_count == k: res += n - j + 1
            if num == max_num:
                max_count -= 1
        return res