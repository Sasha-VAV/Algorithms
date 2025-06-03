from typing import List
from collections import deque


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque(initialBoxes)
        res = 0
        while q:
            i = q.popleft()
            if status[i] == 0:
                status[i] = 2
                continue
            if status[i] % 2 == 0:
                continue
            status[i] = 4
            for key in keys[i]:
                if status[key] == 0:
                    status[key] = 1
                elif status[key] == 2:
                    status[key] = 3
                    q.append(key)
            for box in containedBoxes[i]:
                q.append(box)
        for i, x in enumerate(status):
            if x == 4: res += candies[i]
        return res