from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        i = 0
        j = 0
        lvl = 0
        state = 0
        skip = False
        while len(res) < m * n:
            if not skip: res.append(matrix[i][j])
            skip = False
            if state == 0:
                j += 1
                if j >= n - lvl - 1:
                    if j == n - lvl:
                        j -= 1
                        skip = True
                    state = 1
            elif state == 1:
                i += 1
                if i >= m - lvl -1:
                    if i == m - lvl:
                        i -= 1
                        skip = True
                    state = 2
            elif state == 2:
                j -= 1
                if j == lvl:
                    state = 3
            elif state == 3:
                i -= 1
                if i == lvl + 1:
                    state = 0
                    lvl += 1
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[3], [2]]))