from typing import List
import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = []
        for num in nums:
            heapq.heappush(numbers, num)
        prev = None
        max_count = 0
        curr_count = 0
        while numbers:
            num = heapq.heappop(numbers)
            if prev is None:
                prev = num - 1
            if num == prev:
                continue
            if num - prev == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 1
            prev = num
        max_count = max(max_count, curr_count)
        return max_count


if __name__ == "__main__":
    nums = [2,20,4,10,3,4,5]
    print(Solution().longestConsecutive(nums))

