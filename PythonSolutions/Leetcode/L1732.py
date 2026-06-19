class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        return max(itertools.accumulate(gains, initial=0))