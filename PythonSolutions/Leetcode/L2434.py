from collections import deque


class Solution:
    def robotWithString(self, s: str) -> str:
        stack = deque()
        res = []
        min_deque = deque()
        for i, c in enumerate(s):
            while min_deque and c < min_deque[-1][0]:
                min_deque.pop()
            min_deque.append((c, i))
        j = 0
        while j < len(s):
            x = min_deque.popleft()[1]
            while stack and stack[-1] <= s[x]:
                res.append(stack.pop())
            res.append(s[x])
            for i in range(j, x):
                stack.append(s[i])
            j = x + 1
        while stack:
            res.append(stack.pop())
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().robotWithString("vzhofnpo"))