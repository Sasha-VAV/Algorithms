class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = deque()
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                curr = 0
                while isinstance(stack[-1], int):
                    curr += stack.pop()
                if curr > 0:
                    curr *= 2
                else:
                    curr = 1
                stack.pop()
                stack.append(curr)
        return sum(stack)