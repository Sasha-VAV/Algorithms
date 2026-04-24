class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        res = 0
        ref = [0] * len(matrix[0])

        for row in matrix:
            for j, x in enumerate(row):
                if x == 1:
                    ref[j] += x
                else:
                    ref[j] = 0

            curr_x = None
            curr = 0
            for j, x in enumerate(sorted(ref, reverse=True)):
                if x == 0:
                    break
                if curr_x is None:
                    curr_x = x
                if curr_x != x:
                    res = max(res, curr)
                    diff = curr_x - x
                    curr -= j * diff
                    curr_x = x
                curr += x
            res = max(res, curr)
        return res


if __name__ == "__main__":
    matrix = [[0,0,1],[1,1,1],[1,0,1]]
    print(Solution().largestSubmatrix(matrix=matrix))