MOD = 10 ** 9 + 7


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        LOG = math.ceil(math.log2(n))

        graph = [list() for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # prune graph
        uplift = [[0] * LOG for _ in range(n + 1)]
        ranks = [-1] * (n + 1)

        curr_rank = -1
        new_q = deque([1])
        q = deque()
        while q or new_q:
            if not q:
                curr_rank += 1
                q = new_q
                new_q = deque()
            while q:
                node = q.pop()
                ranks[node] = curr_rank
                for child in graph[node]:
                    if ranks[child] != -1:
                        uplift[node][0] = child
                    else:
                        new_q.appendleft(child)
        del graph, q, new_q, curr_rank

        # precompute uplift
        for j in range(1, LOG):
            for i in range(1, n + 1):
                uplift[i][j] = uplift[uplift[i][j - 1]][j - 1]

        def lowest_common_ancestor(x, y):
            if ranks[x] > ranks[y]:
                x, y = y, x

            diff = ranks[y] - ranks[x]
            for j in range(LOG):
                if (diff >> j) & 1:
                    y = uplift[y][j]

            if x == y:
                return x

            for j in range(LOG - 1, -1, -1):
                if uplift[x][j] != uplift[y][j]:
                    x = uplift[x][j]
                    y = uplift[y][j]

            return uplift[x][0]

        def calculate_number_of_ways(x, y):
            if x == y:
                return 0
            lca = lowest_common_ancestor(x, y)
            edges = ranks[x] + ranks[y] - 2 * ranks[lca]
            return pow(2, edges - 1, MOD)

        res = []
        for x, y in queries:
            res.append(calculate_number_of_ways(x, y))
        return res
