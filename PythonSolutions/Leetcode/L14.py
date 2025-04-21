class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            if string.startswith(prefix):
                continue
            i = len(prefix)
            while i > 0:
                if string.startswith(prefix[:i]):
                    prefix = prefix[:i]
                    break
                i -= 1
            else:
                return ""
        return prefix