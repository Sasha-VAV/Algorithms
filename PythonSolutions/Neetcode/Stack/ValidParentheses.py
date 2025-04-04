from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif not stack or parentheses[stack.pop()] != c:
                return False
        return not stack


if __name__ == '__main__':
    s = "()[]{}([)]"
    print(Solution().isValid(s))


