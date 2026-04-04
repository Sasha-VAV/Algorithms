class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        prev = 0
        curr_c = None
        curr = 0
        for c in s:
            if c != curr_c:
                res += min(prev, curr)
                prev = curr
                curr = 0
                curr_c = c
            curr += 1
        res += min(prev, curr)
        return res


if __name__ == '__main__':
    string = "00110011"
    print(Solution().countBinarySubstrings(string))