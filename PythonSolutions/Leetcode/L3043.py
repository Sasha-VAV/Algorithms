class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ref = set()
        for x in arr1:
            prefix = ""
            for c in str(x):
                prefix += c
                ref.add(prefix)
        res = 0
        for x in arr2:
            curr = str(x)
            if len(curr) <= res:
                continue
            prefix = curr[:res]
            for c in curr[res:]:
                prefix += c
                if prefix not in ref:
                    break
                res = max(res, len(prefix))
        return res