from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        distances = [float('inf')] * n
        distances[k - 1] = 0
        heap = [(0, k - 1)]

        while heap:
            distance, node = heapq.heappop(heap)
            if distances[node] < distance:
                continue
            for v, w in graph[node]:
                if (d := distance + w) < distances[v]:
                    distances[v] = d
                    heapq.heappush(heap, (d, v))
        res = max(distances)
        if res == float('inf'):
            return -1
        return res


if __name__ == '__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print(Solution().networkDelayTime(times, n, k))