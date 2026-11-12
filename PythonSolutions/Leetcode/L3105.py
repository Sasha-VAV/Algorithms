class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        curr_switch = 0 # -1 decreasing, 0 - eq, 1 - increasing
        curr = 0
        res = 0
        for num in nums:
            if num > prev:
                new_switch = 1
            elif num == prev:
                new_switch = 0
                res = max(curr, res)
                curr = -1
            else:
                new_switch = -1
            if new_switch == curr_switch:
                curr += 1
            else:
                res = max(curr, res)
                curr = 1
            prev = num
            curr_switch = new_switch
        return max(res, curr) + 1
            