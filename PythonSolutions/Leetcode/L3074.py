class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        for i, c in enumerate(capacity):
            apples -= c
            if apples <= 0: return i + 1
        return -1