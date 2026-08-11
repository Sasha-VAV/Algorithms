class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        curr_sum = 0
        prev = nums[0] - 1
        prefix_ended = False
        mem = [0] * 51

        for num in nums:
            if not prefix_ended and num - 1 == prev:
                curr_sum += num
                prev = num
            else:
                prefix_ended = True
            
            mem[num] += 1

        for i in range(curr_sum, curr_sum + 50):
            if i < len(mem) and mem[i] == 0:
                return i
            elif i >= len(mem):
                return i
        raise NotImplementedError
