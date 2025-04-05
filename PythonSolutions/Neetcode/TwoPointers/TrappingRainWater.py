from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = 1
        tmp = 0
        while j < len(height):
            if height[i] <= height[j]:
                area += tmp
                tmp = 0
                i = j
                j += 1
            elif height[i] > height[j]:
                tmp += height[i] - height[j]
                j += 1
        tmp = 0
        j -= 1
        while i < j and height[j - 1] > height[j]:
            j -= 1
        while i < j:
            tmp += max(height[j] - height[i], 0)
            i += 1
        area += tmp
        return area


if __name__ == '__main__':
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))