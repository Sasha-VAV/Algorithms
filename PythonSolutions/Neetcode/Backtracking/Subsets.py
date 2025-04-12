from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**len(nums)):
            mask = bin(i)[2:].rjust(len(nums), '0')
            tmp = []
            for j, c in enumerate(mask):
                if c == '1':
                    tmp.append(nums[j])
            res.append(tmp)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))