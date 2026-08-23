class Solution:
    def sumGame(self, num: str) -> bool:
        sum_l = query_l = 0
        sum_r = query_r = 0
        n = len(num)

        for i, c in enumerate(num):
            if c == "?":
                if i < n // 2:
                    query_l += 1
                else:
                    query_r += 1
            else:
                if i < n // 2:
                    sum_l += int(c)
                else:
                    sum_r += int(c)
            
        if (query_l + query_r) % 2:
            return True # Alice has the final vote
            
        return (sum_l - sum_r) != (query_r - query_l) // 2 * 9