class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda x: (x[1], x[0]))
        indices = list(range(len(queries)))
        indices.sort(key=lambda x: queries[x])
        last_used = {}
        i = 0
        j = 0
        m = len(logs)
        res = [-1] * len(queries)
        for idx in indices:
            query = queries[idx]
            while j < m and logs[j][1] <= query:
                server_id, time = logs[j]
                if query - time <= x:
                    last_used[server_id] = time
                j += 1
                
            while i < m and logs[i][1] + x < query:
                server_id, time = logs[i]
                if last_used[server_id] + x < query:
                    last_used.pop(server_id)
                i += 1
                
            res[idx] = n - len(last_used)
        return res


if __name__ == "__main__":
    n = 6
    logs = [[1,21]]
    x = 10
    queries = [24,35,28,26,20,25,16,31,12]
    print(Solution().countServers(n, logs, x, queries))