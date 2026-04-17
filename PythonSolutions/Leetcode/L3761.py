class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        default_value = len(nums) + 1
        indices = {}
        @cache
        def integer_reverse(x):
            return int(str(x)[::-1])
        res = default_value
        for i, num in enumerate(nums):
            if num in indices:
                res = min(res, i - indices[num])
            indices[integer_reverse(num)] = i
        return res if res < default_value else -1