import heapq
from collections import defaultdict


class Solution:
    def medianSlidingWindow(self, nums: list[int], x: int) -> list[float]:
        n = len(nums)
        medians = [0] * (n - x + 1)
        # using 2 heaps with balancing, upper heap 1st value - median
        lower_heap = []
        upper_heap = []
        
        # lazy deletion
        delayed_deletions = defaultdict(int)
        delayed_lower = 0
        delayed_upper = 0

        x_dec = x - 1
        for i, num in enumerate(nums):
            if not lower_heap or -lower_heap[0] >= num:
                heapq.heappush(lower_heap, -num)
            else:
                heapq.heappush(upper_heap, num)
            if i < x_dec:
                continue
            # rebalancing heaps upper can contain one extra
            while len(lower_heap) - delayed_lower < len(upper_heap) - delayed_upper - 1 or upper_heap and delayed_deletions[upper_heap[0]]:
                val = heapq.heappop(upper_heap)
                if delayed_deletions[val]:
                    delayed_deletions[val] -= 1
                    delayed_upper -= 1
                else:
                    heapq.heappush(lower_heap, -val)

            while len(lower_heap) - delayed_lower > len(upper_heap) - delayed_upper or lower_heap and delayed_deletions[-lower_heap[0]]:
                val = -heapq.heappop(lower_heap)
                if delayed_deletions[val]:
                    delayed_deletions[val] -= 1
                    delayed_lower -= 1
                else:
                    heapq.heappush(upper_heap, val)
            if x & 1:
                median = upper_heap[0]
            else:
                median = (upper_heap[0] + -lower_heap[0]) / 2
            medians[i - x_dec] = median
            num = nums[i - x_dec]
            delayed_deletions[num] += 1
            if num < median:
                delayed_lower += 1
            else:
                delayed_upper += 1
        return medians


if __name__ == "__main__":
    nums = [1,4,2,3]
    x = 4
    print(Solution().medianSlidingWindow(nums, x))