class Solution:
    def rotatedDigits(self, n: int) -> int:
        distinct = "2569"
        equal = "018"
        def is_number_unique(x):
            any_distinct = False
            for c in str(x):
                if c in distinct:
                    any_distinct = True
                elif c not in equal:
                    return False
            return any_distinct
                
        res = 0

        for i in range(1, n + 1):
            if is_number_unique(i):
                res += 1
        return res