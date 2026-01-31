class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_char = 400
        for c in letters:
            if c > target:
                min_char = min(ord(c), min_char)
        if min_char == 400:
            return letters[0]
        return chr(min_char)