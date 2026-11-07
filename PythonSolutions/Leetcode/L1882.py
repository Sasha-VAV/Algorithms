class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        working_servers = []
        available_servers = []
        for idx, server in enumerate(servers):
            heapq.heappush(available_servers, (server, idx))
        n = len(tasks)
        res = [-1] * n
        q = deque()
        j = 0
        while j < n or q:
            while working_servers and working_servers[0][0] <= j:
                server_id = heapq.heappop(working_servers)[1]
                heapq.heappush(available_servers, (servers[server_id], server_id))
            if j < n:
                q.append((tasks[j], j))
            while q and available_servers:
                task, task_id = q.popleft()
                _, server_id = heapq.heappop(available_servers)
                heapq.heappush(working_servers, (j + task, server_id))
                res[task_id] = server_id
            if j < n:
                j += 1
            else:
                j = working_servers[0][0]
        return res