from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]
        for i in range(1, len(triangle)):
            dp.append(dp[-1])
            new_dp = dp.copy()
            for j in range(len(triangle[i])):
                if j == 0:
                    new_dp[0] += triangle[i][j]
                    continue
                new_dp[j] = min(dp[j] + triangle[i][j], dp[j-1] + triangle[i][j])
            dp = new_dp
        return min(dp)


if __name__ == '__main__':
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))