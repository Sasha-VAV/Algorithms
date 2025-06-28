from typing import List
import heapq


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
        res = heapq.nsmallest(k, heap)
        res = sorted(res, key=lambda x: x[1])
        return [x for x, _ in res]