class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        link = [-1] * n
        stack = deque()
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                link[i] = j
                link[j] = i

        res = []
        i = 0
        dr = 1
        while i < n:
            if s[i] in "()":
                dr = -dr
                i = link[i]
            else:
                res.append(s[i])
            i += dr
        return "".join(res)


