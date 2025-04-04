from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        results = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                idx = stack.pop()
                results[idx] = i - idx
            stack.append(i)

        return results


if __name__ == '__main__':
    print(Solution().dailyTemperatures([7,1,3,6,6,5,4,8]))
