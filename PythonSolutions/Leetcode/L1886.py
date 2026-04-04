class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def check_is_equal(arr1, arr2):
            if len(arr1) != len(arr2): return False
            for row1, row2 in zip(arr1, arr2):
                if len(row1) != len(row2): return False
                for x, y in zip(row1, row2):
                    if x != y: return False
            return True
        if check_is_equal(mat, target): return True
        for _ in range(3):
            mat = list(zip(*mat[::-1]))
            if check_is_equal(mat, target): return True
        return False