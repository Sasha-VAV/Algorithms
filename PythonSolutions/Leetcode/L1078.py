class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        res = []
        if len(words) < 3:
            return res
        state = 0
        prev1 = words[0]
        prev2 = words[1]
        for word in words[2:]:
            if prev1 == first and prev2 == second:
                res.append(word)
            prev1, prev2 = prev2, word
        return res