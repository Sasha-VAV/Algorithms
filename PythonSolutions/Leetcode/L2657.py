from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        left = set()
        right = set()
        curr = 0
        res = []
        for a, b in zip(A, B):
            if a in right:
                curr += 1
                right.remove(a)
            else:
                left.add(a)
            if b in left:
                curr += 1
                left.remove(b)
            else:
                right.add(b)
            res.append(curr)
        return res
