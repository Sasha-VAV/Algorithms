from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        heap = sorted(counter.values(), reverse=True)
        res = 0
        for i in range(0, len(heap), 8):
            res += sum(heap[i:i+8]) * (i // 8 + 1)
        return res