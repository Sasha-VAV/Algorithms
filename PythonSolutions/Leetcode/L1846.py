class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for x in arr:
            if x > prev:
                prev += 1
        return prev
