from typing import List
from collections import deque
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        q = deque()
        for x, y in meetings:
            q.appendleft((x, y-x))
        heap = [(0, i) for i in range(n)]
        heapq.heapify(heap)
        i = 0
        res = [0] * n
        while True:
            while q and i >= q[-1][0] and i >= heap[0][0]:
                while i > heap[0][0]:
                    heapq.heappush(heap, (i, heapq.heappop(heap)[1]))
                _, z = heapq.heappop(heap)
                x, y = q.pop()
                res[z] += 1
                heapq.heappush(heap, (i + y, z))
            if not q: break
            i = max(q[-1][0], heap[0][0])
        x = max(res)
        for i, y in enumerate(res):
            if x == y: return i
        return -1


if __name__ == '__main__':
    n = 4
    meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]
    print(Solution().mostBooked(n, meetings))