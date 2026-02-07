class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = len(s)
        curr = 0
        after = s.count("a")
        for c in s:
            res = min(curr + after, res)
            if c == "a":
                after -= 1
            else:
                curr += 1
        return min(curr + after, res)

