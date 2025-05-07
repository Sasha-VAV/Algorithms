class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] * 1001
        for citation in citations:
            counts[citation] += 1
        running_sum = 0
        for h, count in enumerate(counts[::-1]):
            running_sum += count
            if running_sum >= 1000 - h:
                return 1000 - h
        return 0