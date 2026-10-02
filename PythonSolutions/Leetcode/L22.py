class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(start, end, s):
            nonlocal res
            if start == 0 and end == 1:
                res.append(s + ")")
                return
            if start > 0 and end >= 1:
                dfs(start - 1, end, s + "(")
            
            if end > start:
                dfs(start, end - 1, s + ")")
        dfs(n, n, "")
        