class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for x, y, c in roads:
            graph[x][y] = min(c, graph[x][y])
            graph[y][x] = min(c, graph[y][x])
        
        min_achieved = float('inf')
        end_reached = False

        q = deque([1])
        visited = set()

        while q:
            x = q.popleft()
            if x == n:
                end_reached = True

            for y, c in graph[x].items():
                min_achieved = min(min_achieved, c)
                if y not in visited:
                    visited.add(y)
                    q.append(y)
        return min_achieved if end_reached else -1