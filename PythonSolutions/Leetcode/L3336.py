MOD = 10 ** 9 + 7


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        max_num = 201
        dp = [[0] * max_num for _ in range(max_num)]
        dp[0][0] = 1

        for num in nums:
            next_dp = [[0] * max_num for _ in range(max_num)]
            for g1 in range(max_num):
                for g2 in range(max_num):
                    ways = dp[g1][g2]
                    if not ways:
                        continue
                    
                    next_dp[g1][g2] = (next_dp[g1][g2] + ways) % MOD
                    next_g1 = num if not g1 else gcd(g1, num)
                    next_g2 = num if not g2 else gcd(g2, num)

                    next_dp[next_g1][g2] = (next_dp[next_g1][g2] + ways) % MOD
                    next_dp[g1][next_g2] = (next_dp[g1][next_g2] + ways) % MOD
            dp = next_dp
        
        res = 0

        for g in range(1, max_num):
            res = (res + dp[g][g]) % MOD
        
        return res