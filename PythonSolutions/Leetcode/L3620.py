from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = defaultdict(lambda: defaultdict(set))
        for origin, destination, cost in edges:
            if online[destination] and online[origin]:
                graph[origin][destination].add(cost)
        
        def check_possibility(edge_min: int, total: int) -> bool:
            costs = defaultdict(lambda: float('inf'))

            heap = [(0, 0)]

            while heap:
                curr, node = heapq.heappop(heap)
                
                if node == n - 1:
                    return True
                
                for dest, node_costs in graph[node].items():
                    for cost in node_costs:
                        if cost < edge_min or (new_cost := curr + cost) > total or costs[dest] <= new_cost:
                            continue
                        costs[dest] = new_cost
                        heapq.heappush(heap, (new_cost, dest))
            
            return False

        l = 0
        r = k
        max_achieved = -1

        while l <= r:
            mid = l + (r - l) // 2
            if check_possibility(mid, k):
                max_achieved = mid
                l = mid + 1
            else:
                r = mid - 1
        return max_achieved


if __name__ == "__main__":
    edges = [[0,1,5],[0,1,0],[1,2,5]]
    online = [True,True,True]
    k = 10
    print(Solution().findMaxPathScore(edges=edges, online=online, k=k))