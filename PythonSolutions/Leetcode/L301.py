from typing import List
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s):
            q = deque()
            for c in s:
                if c == "(":
                    q.append(c)
                elif c == ")":
                    if q and q[-1] == "(":
                        q.pop()
                    else:
                        q.append(c)
            return len(q)
        m = check(s)
        res = []
        def recursion(s, i, r):
            nonlocal res
            if len(s) < i:
                return
            if len(s) == i:
                if check(s) == 0 and s not in res:
                    res.append(s)
                return
            if r > 0 and s[i] in ["(", ")"]:
                recursion(s[:i]+s[i+1:], i, r-1)
            recursion(s, i+1, r)
            return
        recursion(s, 0, m)
        return res


if __name__ == '__main__':
    s = ")("
    print(Solution().removeInvalidParentheses(s))