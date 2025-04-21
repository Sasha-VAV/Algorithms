class Solution:
    def countAndSay(self, n: int) -> str:
        x = "1"
        for i in range(2, n+1):
            res = ""
            curr = x[0]
            k = 1
            for c in x[1:]:
                if c == curr:
                    k += 1
                else:
                    res += str(k)+curr
                    k = 1
                    curr = c
            res += str(k) + curr
            x = res
        return x


if __name__=="__main__":
    print(Solution().countAndSay(4))