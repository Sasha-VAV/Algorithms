from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([q/w, q] for q, w in zip(quality, wage))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k: qsum += heapq.heappop(heap)
            if len(heap) == k: res = min(res, r * qsum)
        return res