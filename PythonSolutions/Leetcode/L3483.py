class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = [0] * 10
        for digit in digits:
            counts[digit] += 1

        res = 0
        for x in range(100, 1000, 2):
            i, j, k = x // 100, x % 100 // 10, x % 10
            limit_reached = False
            for y in i, j, k:
                if counts[y] <= 0:
                    limit_reached = True
                counts[y] -= 1
            if not limit_reached:
                res += 1
            for y in i, j, k:
                counts[y] += 1
        
        return res

