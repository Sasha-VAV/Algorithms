class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        d = deque(matrix[0][:-1])
        for row in matrix[1:]:
            if list(d) != row[1:]:
                return False
            d.appendleft(row[0])
            d.pop()
        return True