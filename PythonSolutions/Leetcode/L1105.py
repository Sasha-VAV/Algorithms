from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] * len(books)
        for i, (t, h) in enumerate(books):
            if i == 0:
                dp[0] = h
                continue
            dp[i] = dp[i-1] + h
            x = shelfWidth - t
            max_h = h
            j = i
            while j > 0:
                j -= 1
                t, h = books[j]
                x -= t
                if x < 0:
                    break
                max_h = max(h, max_h)
                if j > 0:
                    dp[i] = min(dp[j-1] + max_h, dp[i])
                else:
                    dp[i] = min(max_h, dp[i])
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minHeightShelves(books=[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth=4))