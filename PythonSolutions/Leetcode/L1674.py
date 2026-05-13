class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)
        for i in range(len(nums) // 2):
            a = nums[i]
            b = nums[-i - 1]
            
            diff[2] += 2 # min target +2 for sum
            diff[-1] -= 2 # last target

            low = min(a, b) + 1 # min reachable within one change
            high = max(a, b) + limit # max reachable within one change
            
            diff[low] -= 1
            diff[high +  1] += 1

            diff[a + b] -= 1
            diff[a + b + 1] += 1
        
        res = float('inf')
        curr = 0
        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            res = min(res, curr)
        return res