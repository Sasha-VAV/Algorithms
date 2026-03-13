class Solution:
    def minNumberOfSeconds(self, height: int, workers: List[int]) -> int:
        heap = []
        for i, worker in enumerate(workers):
            heapq.heappush(heap, (worker, i, 2))
        res = 0
        while height:
            work, i, count = heapq.heappop(heap)
            res = max(res, work)
            heapq.heappush(heap, (work + workers[i] * count, i, count+1))
            height -= 1
        return res