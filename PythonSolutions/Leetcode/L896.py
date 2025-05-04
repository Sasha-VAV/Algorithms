class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        prev = nums[0]
        is_incr = None
        for num in nums[1:]:
            if num == prev:
                continue
            if is_incr is None:
                is_incr = num > prev
            if is_incr and num < prev:
                return False
            if not is_incr and num > prev:
                return False
            prev = num
        return True