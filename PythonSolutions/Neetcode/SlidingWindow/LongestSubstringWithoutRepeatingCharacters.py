class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i = 0
        max_len = 0
        for j, c in enumerate(s):
            if c in chars:
                max_len = max(max_len, len(chars))
                while s[i] != c:
                    chars.remove(s[i])
                    i += 1
                i += 1
            chars.add(c)
        max_len = max(max_len, len(chars))
        return max_len


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
