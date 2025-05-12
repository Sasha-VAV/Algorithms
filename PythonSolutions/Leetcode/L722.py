class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        state = 0

        def process(s, state):
            if state == 0:
                i = s.find("//")
                a = s.find("/*")
                if (i < a or a == -1) and i != -1:
                    return s[:i], 0
                if a != -1:
                    c, b = process(s[a + 2:], 1)
                    return s[:a] + c, b
                return s, 0
            i = s.find("*/")
            if i == -1:
                return "", 1
            return process(s[i + 2:], 0)

        state = 0
        sub = ""
        for string in source:
            string, state = process(string, state)
            sub += string
            if sub and state == 0:
                res.append(sub)
                sub = ""
        return res