class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        stack = 0
        max_depth = 0
        for c in seq:
            if c == "(":
                stack += 1
                max_depth = max(max_depth, stack)
            else:
                stack -= 1
        curr_depth = 0
        target = (max_depth + 1) // 2
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == "(":
                if curr_depth >= target:
                    res[i] = 1
                curr_depth += 1
            else:
                if curr_depth > target:
                    res[i] = 1
                curr_depth -= 1
            
        return res