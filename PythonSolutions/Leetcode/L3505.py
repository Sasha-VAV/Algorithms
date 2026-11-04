import heapq
from collections import defaultdict


class Solution:
    def _get_balances(self, nums: list[int], x: int) -> list[int]:
        n = len(nums)
        arrays = [0] * (n - x + 1)
        # using 2 heaps with balancing, upper heap 1st value - median
        lower_heap = []
        upper_heap = []
        
        # maintain sums
        lower_heap_sum = 0
        upper_heap_sum = 0

        # lazy deletion
        delayed_deletions = defaultdict(int)
        delayed_lower = 0
        delayed_upper = 0

        x_dec = x - 1
        for i, num in enumerate(nums):
            if not lower_heap or -lower_heap[0] >= num:
                heapq.heappush(lower_heap, -num)
                lower_heap_sum += num
            else:
                heapq.heappush(upper_heap, num)
                upper_heap_sum += num
            if i < x_dec:
                continue
            # rebalancing heaps upper can contain one extra
            while len(lower_heap) - delayed_lower < len(upper_heap) - delayed_upper - 1 or upper_heap and delayed_deletions[upper_heap[0]]:
                val = heapq.heappop(upper_heap)
                upper_heap_sum -= val
                if delayed_deletions[val]:
                    delayed_deletions[val] -= 1
                    delayed_upper -= 1
                    upper_heap_sum += val
                else:
                    heapq.heappush(lower_heap, -val)
                    lower_heap_sum += val

            while len(lower_heap) - delayed_lower > len(upper_heap) - delayed_upper:
                val = -heapq.heappop(lower_heap)
                lower_heap_sum -= val
                if delayed_deletions[val]:
                    delayed_deletions[val] -= 1
                    delayed_lower -= 1
                    lower_heap_sum += val
                else:
                    heapq.heappush(upper_heap, val)
                    upper_heap_sum += val
        
            median = upper_heap[0]
            arrays[i - x_dec] = upper_heap_sum - lower_heap_sum - median * (x & 1)
            num = nums[i - x_dec]
            delayed_deletions[num] += 1
            if num < median:
                lower_heap_sum -= num
                delayed_lower += 1
            else:
                upper_heap_sum -= num
                delayed_upper += 1
        return arrays

    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        x_dec = x - 1        
        arrays = self._get_balances(nums, x)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 2)] # pos, k
        dp[0][0] = 0
        for i in range(n - x_dec):
            for j in range(k):
                if i > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j])
                dp[i + x][j + 1] = min(dp[i + x][j + 1], dp[i][j] + arrays[i])
        return min(dp[j][-1] for j in range(n + 2))


if __name__ == "__main__":
    nums = [5,5,6,-19]
    x = 2
    k = 1
    print(Solution().minOperations(nums, x, k))