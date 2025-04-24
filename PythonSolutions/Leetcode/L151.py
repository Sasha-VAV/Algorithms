# Any lang solution
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = -1
        for k, c in enumerate(s):
            if c == " ":
                if i != -1:
                    words.append(s[i:k])
                    i = -1
            elif i == -1:
                i = k
        if i != -1:
            words.append(s[i:])
        return " ".join(words[::-1])

# Cheater solution (works better)
class Solution2:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return " ".join(arr[::-1])
