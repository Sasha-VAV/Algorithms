class Solution:
    def minimumTotalDistance(self, robots: List[int], factory: List[List[int]]) -> int:
        robots.sort()
        factory.sort()
        factories = []
        for pos, limit in factory:
            for _ in range(limit):
                factories.append(pos)
        
        n = len(robots)
        m = len(factories)

        next_dist = [0 for _ in range(m + 1)]
        curr = [0 for _ in range(m + 1)]
        curr[m] = float('inf')

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                assign = (
                    abs(robots[i] - factories[j]) + next_dist[j + 1]
                )
                skip = curr[j + 1]
                curr[j] = min(assign, skip)
            next_dist = curr[:]
        
        return curr[0]