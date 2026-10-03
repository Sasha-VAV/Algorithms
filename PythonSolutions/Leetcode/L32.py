class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = deque()
        last_invalid = -1
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if not stack:
                    last_invalid = i
                else:
                    res = max(res, i - stack.pop() + 1)
            if not stack:
                res = max(res, i - last_invalid)
            else:
                res = max(res, i - stack[-1])
        return res