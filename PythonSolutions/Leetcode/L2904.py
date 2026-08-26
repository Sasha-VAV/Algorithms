class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        count = 0
        res = None
        # I could make solution with bit as number to optimize, but not needed
        for j, c in enumerate(s):
            if c == "1":
                count += 1

            if count == k:
                while i < j and s[i] == "0":
                    i += 1
                if res is None or j - i + 1 < len(res):
                    res = s[i:j + 1]
                elif j - i + 1 == len(res):
                    res = min(s[i:j+1], res)
                i += 1
                count -= 1
                while i < j and s[i] == "0":
                    i += 1
        return "" if res is None else res


if __name__ == "__main__":
    s = "01011101000111110"
    k = 5
    print(Solution().shortestBeautifulSubstring(s, k))