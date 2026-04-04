class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if len(s) - i <= res:
                break
            count = defaultdict(int)
            for j in range(i, len(s)):
                count[s[j]] += 1
                if j - i + 1 <= res: continue
                prev = None
                for k, v in count.items():
                    if prev is None:
                        prev = v
                    if v != prev:
                        break
                else:
                    res = max(res, j - i + 1)
        return res