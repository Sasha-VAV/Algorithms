from typing import List


class Solution:
    def partition(self, s: str, is_first=True) -> List[List[str]]:
        res = [[]]
        for i in range(len(s)):
            tmp = s[:i+1]
            if tmp == tmp[::-1]:
                a = self.partition(s[i+1:], is_first=False)
                req_len = len(s) - i - 1
                a = [[tmp] + b for b in a if len("".join(b)) == req_len]
                res.extend(a)
        return res[1:] if is_first else res


if __name__ == '__main__':
    print(Solution().partition('cdd'))