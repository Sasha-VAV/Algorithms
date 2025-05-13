from typing import List
from collections import deque


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = deque()
        res = [0] * n
        for log in logs:
            a, b, c = log.split(":")
            a, c = int(a), int(c)
            if b == "start":
                if stack:
                    res[stack[-1][0]] += c - stack[-1][1]
                stack.append((a, c))
            else:
                b = stack.pop()
                res[b[0]] += c - b[1] + 1
                if stack:
                    stack[-1] = (stack[-1][0], c + 1)
        return res


if __name__ == '__main__':
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    print(Solution().exclusiveTime(n, logs))