from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def lower_border(nums, value):
            i = 0
            j = len(nums) - 1
            res = 0
            while i <= j:
                if nums[i] + nums[j] < value:
                    res += j - i
                    i += 1
                else:
                    j -= 1
            return res
        return lower_border(nums, upper+1) - lower_border(nums, lower)



if __name__ == '__main__':
    print(Solution().countFairPairs([6,9,4,2,7,5,10,3], 13, 13))