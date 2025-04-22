from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11 = rec1[0]
        y11 = rec1[1]
        x12 = rec1[2]
        y12 = rec1[3]
        x21 = rec2[0]
        y21 = rec2[1]
        x22 = rec2[2]
        y22 = rec2[3]
        ...