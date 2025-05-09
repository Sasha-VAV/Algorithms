from typing import List
from collections import deque


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def cartesian_product(set1, set2):
            new_set = set()
            for a in set1:
                for b in set2:
                    new_set.add(a + b)
            return new_set
        stack = deque()
        for c in expression:
            if c != "}":
                if c.isalpha() and stack and isinstance(stack[-1], set):
                    stack.append(cartesian_product(stack.pop(), {c}))
                elif c.isalpha():
                    stack.append({c})
                else:
                    stack.append(c)
            else:
                x = set()
                prev = None
                while stack[-1] != "{":
                    if stack[-1] == ",":
                        x = x.union(prev)
                        stack.pop()
                        prev = None
                    elif prev is None:
                        prev = stack.pop()
                    else:
                        prev = cartesian_product(stack.pop(), prev)
                stack.pop()
                if prev is not None:
                    x = x.union(prev)
                stack.append(x)
        res = set()
        prev = None
        while stack:
            if stack[-1] == ",":
                res = res.union(prev)
                stack.pop()
                prev = None
            elif prev is None:
                prev = stack.pop()
            else:
                prev = cartesian_product(stack.pop(), prev)
        if prev is not None:
            res = res.union(prev)
        return sorted(list(res))


if __name__ == '__main__':
    print(Solution().braceExpansionII("{a}"))