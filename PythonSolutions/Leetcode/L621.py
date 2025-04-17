from asyncio import tasks
from typing import List
from collections import deque, Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        heap = []
        for k, v in tasks.items():
            heapq.heappush(heap, -v)
        q = deque()
        t = 0
        while heap or q:
            t += 1
            if q and q[0][0] == t:
                _, x = q.popleft()
                heapq.heappush(heap, -x)
            if heap:
                x = -heapq.heappop(heap)
                if x > 1:
                    q.append((t+n+1, x-1))
        return t


if __name__ == '__main__':
    print(Solution().leastInterval(["A","A", "A","B","B", "B"], 2))