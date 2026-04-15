class Solution:
    def closestTarget(self, words: List[str], target: str, start: int) -> int:
        n = len(words)
        for shift in range(n // 2 + 1):
            if words[(start + shift) % n ] == target or words[start - shift] == target:
                return shift
        return -1