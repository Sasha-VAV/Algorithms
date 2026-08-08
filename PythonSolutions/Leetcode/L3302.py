class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        j = m - 1
        dp = [-1] * m

        for i in range(n - 1, -1, -1):
            if j == 0:
                break
            
            if word1[i] == word2[j]:
                dp[j] = i
                j -= 1
        
        res = []
        had_skip = 0
        j = 0
        
        for i, c in enumerate(word1):
            if j == m:
                break
            
            if c == word2[j] or not had_skip and (j == m - 1 or i < dp[j + 1]):
                had_skip += c != word2[j]
                res.append(i)
                j += 1
            

        return res if j == m else []