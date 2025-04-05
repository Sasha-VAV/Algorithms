from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int], is_first=True) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums = nums.copy()
        if is_first:
            nums.insert(0, 0)
        a = nums.copy()
        a.insert(0, a.pop(0) ^ a.pop(0))
        b = nums.copy()
        b.pop(1)
        return self.subsetXORSum(a, False) + self.subsetXORSum(b, False)


if __name__ == '__main__':
    nums = [5,1,6]
    print(Solution().subsetXORSum(nums))

