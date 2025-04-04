from typing import List
from collections import deque


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))
        stack = deque()
        for pos, spd in zip(position, speed):
            stack.append((target - pos) / spd)
        k = 0
        while stack:
            x = stack.pop()
            while stack and x >= stack[-1]:
                stack.pop()
            k += 1
        return k


if __name__ == '__main__':
    target = 10
    position = [1, 4]
    speed = [3, 2]
    print(Solution().carFleet(target, position, speed))
