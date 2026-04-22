class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_edit_possible(str1, str2):
            res = 0
            for c1, c2 in zip(str1, str2):
                if c1 != c2:
                    res += 1
                    if res > 2:
                        return False
            return True
        
        res = []
        for query in queries:
            for ref in dictionary:
                if is_edit_possible(query, ref):
                    res.append(query)
                    break
        return res