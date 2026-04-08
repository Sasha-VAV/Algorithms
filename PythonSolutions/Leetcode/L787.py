class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        distances = [{} for _ in range(n)]
        distances[src] = {0: 0}
        heap = [(0, 0, src)]

        while heap:
            distance, num, node = heapq.heappop(heap)
            if node == dst:
                return distance
            if distances[node][num] < distance or num > k:
                continue

            num += 1

            for v, w in graph[node]:
                d = distance + w
                if num not in distances[v] or distances[v][num] > d:
                    distances[v][num] = d
                    heapq.heappush(heap, (d, num, v))
        return -1