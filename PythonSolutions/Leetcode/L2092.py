class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], first_one: int) -> List[int]:
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
                    self.parent[root_x] = root_y
                elif self.rank[root_y] < self.rank[root_x]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_x] = root_y
                    self.rank[root_x] += 1
                
            def met_one(self, x):
                return self.find(x) == self.find(0)
            
            def reset(self, x):
                self.parent[x] = x
                self.rank[x] = 0
                
        uf = UnionFind(n)
        uf.union(0, first_one)
        res = {0, first_one}

        time_frame = []
        current_time = 0
        meetings.append((0, 0, float('inf'))) # To avoid additional logic

        for x, y, c in sorted(meetings, key=lambda x: (x[2], x[0], x[1])):
            if current_time != c:
                current_time = c
                for a in time_frame:
                    if not uf.met_one(a):
                        uf.reset(a)
                    else:
                        res.add(a)
                time_frame.clear()
            time_frame.append(x)
            time_frame.append(y)
            uf.union(x, y)
            
        return list(res)
