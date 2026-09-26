class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = {k: v for k, v in knowledge}
        l = -1
        res = []
        for i, c in enumerate(s):
            if c == "(":
                l = i + 1
            elif c == ")":
                res.append(knowledge.get(s[l:i], "?"))
                l = -1
            elif l == -1:
                res.append(c)
        return "".join(res)