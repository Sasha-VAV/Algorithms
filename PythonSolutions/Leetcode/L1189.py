class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target = Counter(target)
        resources = Counter(s)

        max_copies = 1_000_000
        for k, v1 in target.items():
            v2 = resources[k]
            max_copies = min(max_copies, v2 // v1)
            if max_copies == 0:
                return 0
        return max_copies

    def maxNumberOfBalloons(self, text: str) -> int:
        return self.rearrangeCharacters(text, "balloon")