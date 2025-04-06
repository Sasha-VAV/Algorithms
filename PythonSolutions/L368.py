from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        if nums[0] == 1:
            res.append(nums.pop(0))
        sets = dict()
        for num in nums:
            sets[num] = list()
            for k, v in sets.items():
                if num % k == 0 and len(sets[num]) < len(v) + 1 and k != num:
                    sets[num] = v.copy()
                    sets[num].append(k)

        max_set = None
        for k, v in sets.items():
            if max_set is None or len(v) + 1 > len(max_set):
                max_set = v
                max_set.append(k)
        if max_set is not None:
            res.extend(max_set)
        return res



if __name__ == '__main__':
    nums = [5,9,18,54,108,540,90,180,360,720]
    print(Solution().largestDivisibleSubset(nums))
