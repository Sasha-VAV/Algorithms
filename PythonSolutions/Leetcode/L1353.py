from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        final_time = max(events, key=lambda x: x[1])[1]
        events.sort()
        i = events[0][0]
        j = 0
        heap = []
        res = 0
        while i <= final_time:
            while j < len(events) and events[j][0] == i:
                heapq.heappush(heap, events[j][1])
                j += 1
            if heap:
                res += 1
                heapq.heappop(heap)
            i += 1
            while heap and heap[0] < i:
                heapq.heappop(heap)
        return res


if __name__ == '__main__':
    events = [[1,100000]]
    print(Solution().maxEvents(events))