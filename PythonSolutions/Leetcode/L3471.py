class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        if k == 1:
            counts = [0] * 51
            for num in nums:
                counts[num] += 1

            for i in range(50, 0, -1):
                if counts[i] == 1:
                    return i

        first_num = nums[0]
        last_num = nums[-1]
        counts = [0] * 2

        for num in nums:
            if num == first_num:
                counts[0] += 1
            if num == last_num:
                counts[1] += 1

        if counts[0] > 1 and counts[1] > 1:
            return -1
        if counts[0] == 1 and counts[1] > 1:
            return first_num
        if counts[0] > 1 and counts[1] == 1:
            return last_num
        return max(first_num, last_num)