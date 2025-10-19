class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        strings = set()
        def dfs(string):
            if string in strings: return
            strings.add(string)
            dfs(string[b:] + string[:b])
            dfs("".join([str((int(c) + a) % 10) if i % 2 == 1 else c for i, c in enumerate(string)]))
        dfs(s)
        return min(strings)