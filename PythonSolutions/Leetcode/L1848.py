class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, x in enumerate(nums):
            if x != target:
                continue
            if (tmp := abs(i - start)) < res:
                res = tmp
            else:
                return res
        return res