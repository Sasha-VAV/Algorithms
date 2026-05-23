class Solution:
    def check(self, nums: List[int]) -> bool:
        was_peak = False
        leftmost = nums[0]
        prev = leftmost
        for num in islice(nums, 1, len(nums)):
            if prev > num:
                if was_peak or num > leftmost:
                    break
                else:
                    was_peak = True
            elif was_peak and num > leftmost:
                break
            prev = num
        else:
            return True
        return False