class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        curr = 0
        n = len(lcp)
        res = [-1] * n
        count = n
        i = 0
        while count > 0:
            used_char = False
            if curr >= 26 or i >= n: 
                return ""
            for j in range(n):
                if res[j] != -1:
                    continue
                if lcp[i][j] > 0:
                    res[j] = curr
                    count -= 1
                    used_char = True
            if used_char:
                curr += 1
            i += 1
        
        ref = [[-1] * n for _ in range(n)]
        def find_lcp(source, i, j):
            min_common = min(len(source) - i, len(source) - j)
            for shift in range(min_common):
                if source[i+shift] != source[j+shift]:
                    return shift
            return min_common

        for i in range(n):
            for j in range(n):
                if i > 0 and j > 0 and ref[i-1][j-1] > 0:
                    ref[i][j] = ref[i-1][j-1] - 1
                else:
                    ref[i][j] = find_lcp(res, i, j)
                if ref[i][j] != lcp[i][j]: 
                    return ""
        x = ord("a")
        return "".join(chr(x + y) for y in res)
    

if __name__ == "__main__":
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    print(Solution().findTheString(lcp=lcp))