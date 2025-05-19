class Solution:
    def countSubstrings(self, s: str) -> int:
        i = 0
        j = 0
        k = 0
        n = len(s)
        while i < n:
            j += 1
            if s[i:j] == s[i:j][::-1]:
                k += 1
            if j == n:
                i += 1
                j = i
        return k


if __name__ == '__main__':
    print(Solution().countSubstrings("abc"))