class Solution:
    def clearStars(self, s: str) -> str:
        ref = [1] * len(s)
        chars = [[] for _ in range(26)]
        min_char = 26
        for i, c in enumerate(s):
            if c == "*" and min_char != -1:
                j = chars[min_char].pop()
                ref[j] = 0
                while min_char < 26 and len(chars[min_char]) == 0:
                    min_char += 1
            if c == "*":
                ref[i] = 0
            else:
                j = ord(c) - ord('a')
                chars[j].append(i)
                if j < min_char: min_char = j
        return ''.join([s[i] for i in range(len(ref)) if ref[i]])


if __name__ == '__main__':
    print(Solution().clearStars("d*"))