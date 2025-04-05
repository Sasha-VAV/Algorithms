class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        patience = k
        i = 0
        max_len = 0
        chars = dict()
        n = len(s)
        for j, c in enumerate(s):
            if c != s[i]:
                patience -= 1
            if patience == -1:
                max_len = max(max_len, min(n, chars[s[i]] + k))
                prev = s[i]
                while s[i] == prev:
                    i += 1
                    chars[prev] -= 1
                    if chars[prev] == 0:
                        chars.pop(prev)
                patience = k - sum(chars.values())
                while (patience + chars.get(s[i], 0)) < 0:
                    chars[s[i]] -= 1
                    i += 1
                    patience += 1
                patience += chars.get(s[i], 0)
            chars[c] = chars.get(c, 0) + 1
        max_len = max(max_len, min(n, chars[s[i]] + k))
        return max_len


if __name__ == '__main__':
    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4
    print(Solution().characterReplacement(s, k))
