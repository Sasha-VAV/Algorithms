class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        used = defaultdict(int)
        heap = nums.copy()
        heapq.heapify(heap)

        max_left = nums[0]
        for i, num in enumerate(nums):
            max_left = max(max_left, num)
            while heap and used[heap[0]] > 0:
                used[heap[0]] -= 1
                heapq.heappop(heap)
            used[num] += 1
            
            if not heap:
                break 
            if max_left - heap[0] <= k:
                return i
        return -1