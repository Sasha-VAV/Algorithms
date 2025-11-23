class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = sum(nums)
        nums.sort()
        target = res % 3
        if target == 0: return res
        ones = []
        twos = []
        for num in nums:
            if num % 3 == 1:
                ones.append(num)
            elif num % 3 == 2:
                twos.append(num)
            else:
                continue
            if target == 1 and len(ones) >= 1 and len(twos) >= 2:
                break
            if target == 2 and len(ones) >= 2 and len(twos) >= 1:
                break
        else:
            ones.extend([res, res])
            twos.extend([res, res])
        if target == 1:
            return max(res - ones[0], res - sum(twos[:2]), 0)
        return max(res - twos[0], res - sum(ones[:2]), 0)
