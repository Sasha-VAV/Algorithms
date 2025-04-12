from heapq import heappush, heappop, heappushpop, nsmallest, heapify
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        for _ in range(k - 1):
            heappop(heap)
        return -heap[0]


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 5, 6, 7]
    print(Solution().findKthLargest(nums, 3))