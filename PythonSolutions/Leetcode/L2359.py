from collections import defaultdict, deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = [[] for _ in range(len(edges))]
        for a, b in enumerate(edges):
            graph[a].append(b)
        lut = [[-1, -1] for _ in range(len(edges))]
        def bfs(node, mode):
            q = deque([node])
            lvl = 0
            seen = set()
            while q:
                new_q = deque()
                while q:
                    node = q.popleft()
                    seen.add(node)
                    lut[node][mode] = lvl
                    for child in graph[node]:
                        if child != -1 and child not in seen:
                            new_q.append(child)
                q = new_q
                lvl += 1
        bfs(node1, 0)
        bfs(node2, 1)
        min_distance = float('inf')
        res = -1
        for i, (a, b) in enumerate(lut):
            if a > -1 and b > -1 and max(a,b) < min_distance:
                res = i
                min_distance = max(a,b)
        return res


if __name__ == '__main__':
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    print(Solution().closestMeetingNode(edges, node1, node2))