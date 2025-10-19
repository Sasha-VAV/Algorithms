from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = defaultdict(deque)
        heap = []
        flooded = set()
        for i, rain in enumerate(rains):
            if rain == 0: continue
            lakes[rain].appendleft(i)
        for k, v in lakes.items():
            v.pop()
        res = []
        for rain in rains:
            if rain > 0:
                res.append(-1)
                if rain in flooded: return []
                flooded.add(rain)
                if not lakes[rain]: continue
                heapq.heappush(heap, (lakes[rain].pop(), rain))
                continue
            if heap:
                _, lake = heapq.heappop(heap)
                res.append(lake)
                flooded.remove(lake)
            else:
                res.append(1)
        return res


if __name__ == '__main__':
    arr = [1,2,0,2,3,0,1]
    print(Solution().avoidFlood(arr))