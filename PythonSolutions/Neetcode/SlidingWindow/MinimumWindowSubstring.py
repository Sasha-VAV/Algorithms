class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        min_str = ""
        chars = dict()
        ref_chars = dict()
        for c in t:
            ref_chars[c] = ref_chars.get(c, 0) + 1
        j = 0
        for i, c in enumerate(s):
            if c not in ref_chars:
                continue
            chars[c] = chars.get(c, 0) + 1
            while j < i and (s[j] not in ref_chars or ref_chars.get(s[j]) < chars.get(s[j], 0)):
                if s[j] not in ref_chars:
                    j += 1
                    continue
                chars[s[j]] -= 1
                j += 1
            tmp = s[j:i+1]
            for k in ref_chars.keys():
                if k not in chars or ref_chars[k] > chars[k]:
                    break
            else:
                if len(tmp) < len(min_str) or min_str == "":
                    min_str = tmp
        return min_str


if __name__ == '__main__':
    s = "OUZODYXAZV"
    t = "XYZ"
    print(Solution().minWindow(s, t))
