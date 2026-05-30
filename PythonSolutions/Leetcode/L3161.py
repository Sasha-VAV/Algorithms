from sortedcontainers import SortedSet
from typing import List



class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def _update_recursive(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
            return

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        if idx <= mid:
            self._update_recursive(left_child, start, mid, idx, value)
        else:
            self._update_recursive(right_child, mid + 1, end, idx, value)

        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def update(self, idx, value):
        self._update_recursive(1, 1, self.n, idx, value)

    def _query_recursive(self, node, start, end, left, right):
        if left <= start and end <= right:
            return self.tree[node]

        if end < left or start > right:
            return 0

        mid = (start + end) // 2
        left_value = self._query_recursive(2 * node, start, mid, left, right)
        right_value = self._query_recursive(2 * node + 1, mid + 1, end, left, right)
        return max(left_value, right_value)

    def query(self, left, right):
        return self._query_recursive(1, 1, self.n, left, right)


MAX_VALUE = 50_000


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        tree = SegmentTree(MAX_VALUE)
        tree.update(MAX_VALUE, MAX_VALUE)

        obstacles = SortedSet([0, MAX_VALUE])

        res = []
        for query in queries:
            if query[0] == 1:
                idx = query[1]
                left_idx = obstacles.bisect_left(idx)
                left = obstacles[left_idx - 1]
                right = obstacles[left_idx]
                obstacles.add(idx)
                tree.update(idx, idx - left)
                tree.update(right, right - idx)
            else:
                _, x, size = query
                left_idx = obstacles.bisect_right(x)
                last_obstacle = obstacles[left_idx - 1]
                trailing_gap = x - last_obstacle
                internal_max = tree.query(1, x)
                res.append(max(trailing_gap, internal_max) >= size)
        return res


if __name__ == "__main__":
    queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
    print(Solution().getResults(queries))