from heapq import heappush, heappop, heappushpop
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > self.k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]


if __name__ == '__main__':
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))
    print(kth.add(5))
    print(kth.add(10))
    print(kth.add(9))
    print(kth.add(4))
