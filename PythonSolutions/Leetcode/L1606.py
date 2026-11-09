import heapq
import bisect

from sortedcontainers import SortedSet


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        server_stats = [0] * k
        servers_in_use = []
        available_servers = SortedSet(list(range(k)))
        for i, (arrival, load) in enumerate(zip(arrival, load)):
            while servers_in_use and servers_in_use[0][0] <= arrival:
                available_servers.add(heapq.heappop(servers_in_use)[1])
            if not available_servers:
                continue
            idx = bisect.bisect_left(available_servers, i % k) % len(available_servers)
            server = available_servers[idx]
            available_servers.remove(server)
            server_stats[server] += 1
            heapq.heappush(servers_in_use, (arrival + load, server))
        max_stat = 0
        max_members = []
        for i, x in enumerate(server_stats):
            if x > max_stat:
                max_members = [i]
                max_stat = x
            elif x == max_stat:
                max_members.append(i)
        return max_members


if __name__ == "__main__":
    k = 3
    arrival = [1,2,3,4,5]
    load = [5,2,3,3,3]
    print(Solution().busiestServers(k, arrival, load))