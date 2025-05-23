from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        max_sum = 0
        count = 0
        worst_xor = None
        best_xor = None
        for num in nums:
            if (num ^ k) >= num:
                count += 1
                if worst_xor is None:
                    worst_xor = (num ^ k) - num
                worst_xor = min((num ^ k) - num, worst_xor)
                num = num ^ k
            else:
                if best_xor is None:
                    best_xor = num - (num ^ k)
                best_xor = min(num - (num ^ k), best_xor)
            max_sum += num
        if count % 2 == 1:
            if best_xor is None:
                best_xor = worst_xor
            max_sum -= min(worst_xor, best_xor)
        return max_sum


if __name__ == '__main__':
    nums = [24,78,1,97,44]
    k = 6
    edges = [[0,2],[1,2],[4,2],[3,4]]
    print(Solution().maximumValueSum(nums, k, edges))