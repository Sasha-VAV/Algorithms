class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            area = max(min(height[i], height[j]) * (j - i), area)
        return area