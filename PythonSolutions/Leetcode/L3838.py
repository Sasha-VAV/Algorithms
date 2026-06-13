class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        start_idx = ord('a')
        return "".join(
            (chr(
                25 - (sum(
                    weights[ord(c) - start_idx]
                    for c in word
                )) % 26 + start_idx
            ) for word in words)
        )