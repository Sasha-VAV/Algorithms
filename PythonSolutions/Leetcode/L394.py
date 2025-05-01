from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                stack2 = deque()
                while stack[-1] != "[":
                    stack2.appendleft(stack.pop())
                stack.pop()
                a = deque()
                while stack and stack[-1].isdigit():
                    a.appendleft(stack.pop())
                a = int("".join(list(a)))
                stack.append(a*"".join(list(stack2)))
        return "".join(list(stack))


if __name__ == '__main__':
    print(Solution().decodeString("100[lc]"))