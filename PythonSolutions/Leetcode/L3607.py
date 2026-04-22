from typing import List
from collections import defaultdict
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x, root_y = self.find(x), self.find(y)
                if root_x == root_y:
                    return
                
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = self.parent[root_y]
                elif self.rank[root_y] < self.rank[root_x]:
                    self.parent[root_y] = self.parent[root_x]
                else:
                    self.parent[root_x] = self.parent[root_y]
                    self.rank[root_x] += 1
                
        uf = UnionFind(c)
        for u, v in connections:
            uf.union(u - 1, v - 1)
        
        heaps = defaultdict(list)
        active = defaultdict(set)

        for i in range(c):
            root = uf.find(i)
            heapq.heappush(heaps[root], i)
            active[root].add(i)
        
        res = []
        for c, x in queries:
            x -= 1
            root = uf.find(x)
            if c == 2:
                if x in active[root]:
                    active[root].remove(x)
                continue
            
            if x in active[root]:
                res.append(x + 1)
                continue
            
            heap = heaps[root]
            curr = active[root]
            while heap:
                y = heap[0]
                if y not in curr:
                    heapq.heappop(heap)
                    continue
                res.append(y + 1)
                break
            else:
                res.append(-1)
        return res


if __name__ == "__main__":
    c = 5
    connections = [[1,2],[2,3],[3,4],[4,5]]
    queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
    print(Solution().processQueries(c, connections, queries))