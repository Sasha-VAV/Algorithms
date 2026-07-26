class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        neg_heap = []
        pos_heap = []
        for num in nums:
            heapq.heappush(neg_heap, -num)
            heapq.heappush(pos_heap, num)
            if len(neg_heap) > 2:
                heapq.heappop(neg_heap)
            if len(pos_heap) > 3:
                heapq.heappop(pos_heap)

        neg_product = 1
        pos_product = 1
        while pos_heap:
            if neg_heap:
                neg_product *= heapq.heappop(neg_heap)
            else:
                neg_product *= pos_heap[0]
            pos_product *= heapq.heappop(pos_heap)
        return max(neg_product, pos_product)