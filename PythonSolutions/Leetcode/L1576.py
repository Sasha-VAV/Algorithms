class Solution:
    def modifyString(self, s: str) -> str:
        i = s.find('?')
        n = len(s)
        while i > -1:
            c1 = s[i-1] if i > 0 else "_"
            c2 = s[i+1] if i < n - 1 else "_"
            for c in 'dab':
                if c != c1 and c != c2:
                    s = s[:i] + c + s[i+1:]
                    break
            i = s.find('?', i+1)
        return s