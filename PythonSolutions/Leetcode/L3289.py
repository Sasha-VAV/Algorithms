class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = [0] * (len(nums) - 2)
        res = []
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                res.append(num)
        return res