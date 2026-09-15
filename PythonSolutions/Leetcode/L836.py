class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def lines_overlap(a1, b1, a2, b2) -> bool:
            return min(b1, b2) > max(a1, a2)
            
        return (
            lines_overlap(rec1[0], rec1[2], rec2[0], rec2[2]) and
            lines_overlap(rec1[1], rec1[3], rec2[1], rec2[3])
        )