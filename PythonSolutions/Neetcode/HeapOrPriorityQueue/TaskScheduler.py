import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        task_counts = [-task for task in task_counts]
        k = 0
        heapq.heapify(task_counts)
        queue = deque([-1]*n)
        is_in_queue = 0
        while task_counts or (is_in_queue and queue):
            b = False
            if is_in_queue and queue:
                a = queue.popleft()
                b = True
                if a != -1:
                    is_in_queue -= 1
                    heapq.heappush(task_counts, -a)
            if task_counts:
                a = -heapq.heappop(task_counts)
            else:
                a = -1
            if a > 1:
                queue.append(a - 1)
                is_in_queue += 1
            else:
                queue.append(-1)
            if b or a > 0:
                k += 1
        return k


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 50
    print(Solution().leastInterval(tasks, n))