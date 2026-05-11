class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            for x in str(num):
                res.append(int(x))
        return res