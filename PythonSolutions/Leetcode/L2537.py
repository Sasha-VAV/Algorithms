from typing import List
import math


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        window = dict()
        n = len(nums)
        res = 0
        curr_count = 0
        j = -1
        for i, num in enumerate(nums):
            while curr_count < k:
                j += 1
                if j == n:
                    return res
                if nums[j] in window:
                    a = window[nums[j]]
                    if a != 0:
                        curr_count -= a * (a + 1) // 2
                    window[nums[j]] += 1
                    a += 1
                    if a != 0:
                        curr_count += a * (a + 1) // 2
                    else:
                        curr_count += 1
                else:
                    window[nums[j]] = 0
            res += n - j
            a = window[num]
            if a == 0:
                window.pop(num)
            elif a == 1:
                window[num] = 0
                curr_count -= 1
            else:
                curr_count -= a * (a + 1) // 2
                window[num] -= 1
                a -= 1
                curr_count += a * (a + 1) // 2
        return res


if __name__ == '__main__':
    nums = [1,1,1,1,1]
    print(Solution().countGood(nums, 10))