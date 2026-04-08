from collections import defaultdict
import heapq


class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def count_cities(k):
            # Closure is used, move this method out carefully
            distances = [float('inf')] * n
            distances[k] = 0
            heap = [(0, k)]
            while heap:
                distance, node = heapq.heappop(heap)
                if distance > distances[node]:
                    continue
                for v, w in graph[node]:
                    if (d := distance + w) <= threshold and d < distances[v]:
                        distances[v] = d
                        heapq.heappush(heap, (d, v))
            return sum(d != float('inf') for d in distances) - 1

        arg = None
        value = n
        for i in range(n):
            candidate = count_cities(i)
            if candidate <= value:
                value = candidate
                arg = i
        return arg


if __name__ == '__main__':
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    threshold = 4
    print(Solution().findTheCity(n, edges, threshold))