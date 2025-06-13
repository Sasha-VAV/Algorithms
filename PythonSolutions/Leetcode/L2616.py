from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            i, pairs = 0, 0
            while i < len(nums) - 1 and pairs < p:
                if nums[i+1] - nums[i] <= mid:
                    pairs += 1
                    i += 1
                i += 1
            if pairs == p:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    p = 2
    print(Solution().minimizeMax(nums, p))