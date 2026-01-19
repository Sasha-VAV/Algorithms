class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix[i][j+1] = prefix[i][j] + mat[i][j]

        def check(k):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    curr = 0
                    for shift in range(k):
                        curr += prefix[i+shift][j+k] - prefix[i+shift][j]
                        if curr > threshold:
                            break
                    else:
                        return True
            return False

        res = 0
        l = 1
        r = min(m, n)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res