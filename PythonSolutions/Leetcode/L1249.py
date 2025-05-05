class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c == ')':
                arr = []
                while stack and stack[-1] != '(':
                    arr.append(stack.pop())
                if stack:
                    arr = ["("] + arr[::-1] + [")"]
                    stack.pop()
                else:
                    arr = arr[::-1]
                stack.append(''.join(arr))
            else:
                stack.append(c)
        arr = []
        while stack:
            if stack[-1] != '(':
                arr.append(stack.pop())
            else:
                stack.pop()
        return ''.join(arr[::-1])