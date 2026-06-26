class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefixes = [0] * (2 * n + 1)
        prefixes[n] = 1
        curr_sum = 0
        curr_count = n
        res = 0

        for num in nums:
            if num == target:
                curr_sum += prefixes[curr_count]
                curr_count += 1
            else:
                curr_count -= 1
                curr_sum -= prefixes[curr_count]
            
            prefixes[curr_count] += 1
            res += curr_sum
        return res