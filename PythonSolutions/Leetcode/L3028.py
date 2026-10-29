class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for x in nums:
            curr += x
            res += int(not curr)
        return res
                