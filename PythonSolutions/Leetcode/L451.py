import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        chars = [0] * 123
        for c in s:
            chars[ord(c)] += 1
        heap = []
        for char, count in enumerate(chars):
            if count == 0:
                continue
            heapq.heappush(heap, (-count, chr(char)))
        str_arr = []
        while heap:
            x = heapq.heappop(heap)
            str_arr.append(x[1]*(-x[0]))
        return "".join(str_arr)