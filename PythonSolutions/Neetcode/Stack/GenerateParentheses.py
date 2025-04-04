from typing import List
from collections import deque


class Solution:
    def generateParenthesis(self, n: int, stack=deque(), prefix="") -> List[str]:
        result = []
        if n == 0:
            while stack:
                prefix += ")"
                stack.pop()
            result.append(prefix)
            return result

        new_stack = stack.copy()
        new_stack.append("(")
        result.extend(self.generateParenthesis(n-1, new_stack, prefix + "("))
        if stack:
            new_stack = stack.copy()
            new_stack.pop()
            result.extend(self.generateParenthesis(n, new_stack, prefix + ")"))
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
