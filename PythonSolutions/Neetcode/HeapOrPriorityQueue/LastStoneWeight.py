from heapq import heappush, heappop, heappushpop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        while len(heap) > 1:
            a = -heappop(heap)
            b = -heappop(heap)
            if a != b:
                heappush(heap, b - a)
        return 0 if len(heap) == 0 else -heap[0]


if __name__ == '__main__':
    stones = [2,3,6,2,4]
    print(Solution().lastStoneWeight(stones))