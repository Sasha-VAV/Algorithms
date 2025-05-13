from collections import deque


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        chars = [0] * 26
        for c in s:
            chars[ord(c) - ord("a")] += 1
        chars = deque(chars)
        delimiter = 10**9 + 7
        for _ in range(t):
            x = chars.pop() % delimiter
            chars[0] += x
            chars.appendleft(x)
        return sum(chars) % delimiter