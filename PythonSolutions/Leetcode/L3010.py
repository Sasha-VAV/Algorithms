class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        heap = []
        for num in nums[1:]:
            heapq.heappush(heap, -num)
            if len(heap) > 2:
                heapq.heappop(heap)
        while heap:
            res -= heapq.heappop(heap)
        return res