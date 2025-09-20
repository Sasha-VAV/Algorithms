from collections import Counter
import heapq


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        heap = []
        res = 0
        for _, v in counter.items():
            heapq.heappush(heap, v)
            if len(heap) > k:
                res += heapq.heappop(heap)
        return res