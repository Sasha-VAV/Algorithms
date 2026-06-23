MOD = 10 ** 9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        r = r - l + 1
        dp0 = [1] * r
        dp1 = [1] * r

        for _ in range(1, n):
            next_dp0 = [0] * r
            next_dp1 = [0] * r
            pref = 0
            suff = 0
            for i in range(r):
                next_dp0[i] = pref
                next_dp1[-i - 1] = suff

                pref = (pref + dp1[i]) % MOD
                suff = (suff + dp0[-i - 1]) % MOD
                
            dp0 = next_dp0
            dp1 = next_dp1
            
            
        return (sum(dp0) + sum(dp1)) % MOD


if __name__ == "__main__":
    print(Solution().zigZagArrays(3, 1, 3))