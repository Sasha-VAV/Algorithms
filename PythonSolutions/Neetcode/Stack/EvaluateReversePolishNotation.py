from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(eval(f"{a}{token}{b}")))
            else:
                stack.append(token)
        return int(stack.pop())


if __name__ == '__main__':
    tokens = ["12"]
    print(Solution().evalRPN(tokens))
