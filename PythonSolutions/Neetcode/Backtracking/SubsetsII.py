from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        i = 0
        while i < len(nums):
            tmp = [[nums[i]]]
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
                tmp.append(tmp[-1] + [nums[i]])
            tmp = [r + t for t in tmp for r in res]
            res.extend(tmp)
            i += 1
        return res


if __name__ == '__main__':
    nums = [1, 2, 1]
    print(Solution().subsetsWithDup(nums))