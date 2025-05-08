class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        res = 0
        for i, h in enumerate(heights):
            if not stack or h > stack[-1][0]:
                stack.append((h, i))
                continue
            b = i
            while stack and h <= stack[-1][0]:
                if h == stack[-1][0]:
                    break
                a, b = stack.pop()
                res = max(res, a * (i - b))
            else:
                stack.append((h, b))
        n = len(heights)
        while stack:
            a, b = stack.pop()
            res = max(res, a * (n - b))
        return res