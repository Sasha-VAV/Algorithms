class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        possible = ["(", "[", "{"]
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in possible:
                stack.append(c)
            else:
                if not stack or pairs[c] != stack.pop():
                    return False
        return not stack
