from collections import deque


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = deque()
        res = ""
        tmp = ""
        for c in s:
            if c == "(":
                if stack:
                    tmp += c
                stack.append(c)
            else:
                if len(stack) > 1:
                    tmp += ")"
                else:
                    res += tmp
                    tmp = ""
                stack.pop()
        return res


if __name__ == '__main__':
    print(Solution().removeOuterParentheses("(()())(())(()(()))"))