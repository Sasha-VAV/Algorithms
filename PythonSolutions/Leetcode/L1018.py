class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        res = []
        for num in nums:
            curr = curr*2 + num
            res.append(curr % 5 == 0)
        return res