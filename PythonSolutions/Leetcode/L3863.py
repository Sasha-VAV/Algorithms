class Solution:
    def minOperations(self, s: str) -> int:
        min_char_idx = 0
        min_char = s[0]
        max_char_idx = 0
        max_char = s[0]
        prev = s[0]
        violated = False
        for i, c in enumerate(s):
            if c < min_char:
                min_char = c
                min_char_idx = i
            if c >= max_char:
                max_char = c
                max_char_idx = i
            if c < prev:
                violated = True
            prev = c
        if not violated: # Already sorted
            return 0
        if len(s) == 2: # Impossible to sort
            return -1
        last_idx = len(s) - 1
        if min_char_idx == 0 or max_char_idx == last_idx: # One ovelap enough
            return 1
        if min_char_idx == last_idx and max_char_idx == 0: # 3 overlaps
            return 3
        return 2

