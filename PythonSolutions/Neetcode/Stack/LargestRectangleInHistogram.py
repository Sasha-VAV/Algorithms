from typing import List
from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        areas = [0] * len(heights)
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                idx = stack.pop()
                if stack:
                    areas[idx] = (i - stack[-1] - 1) * heights[idx]
                else:
                    areas[idx] = i * heights[idx]
            stack.append(i)
        while stack:
            idx = stack.pop()
            if stack:
                areas[idx] = (len(heights) - stack[-1] - 1) * heights[idx]
            else:
                areas[idx] = len(heights) * heights[idx]
        return max(areas)


if __name__ == '__main__':
    heights=[7,1,7,2,2,4]
    print(Solution().largestRectangleArea(heights))