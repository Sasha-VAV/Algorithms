MODULO = 10 ** 9 + 7
MAX = 10 ** 5 + 1
powers = [1] * MAX
for i in range(1, MAX):
    powers[i] = (powers[i - 1] * 10) % MODULO

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_sum = [0] * (n + 1)
        prefix_number = [0] * (n + 1)
        prefix_len = [0] * (n + 1)

        for i, x in enumerate(map(int, s)):
            if x == 0:
                prefix_sum[i + 1] = prefix_sum[i]
                prefix_number[i + 1] = prefix_number[i]
                prefix_len[i + 1] = prefix_len[i]
            else:
                prefix_sum[i + 1] = prefix_sum[i] + x
                prefix_number[i + 1] = (prefix_number[i] * 10 + x) % MODULO
                prefix_len[i + 1] = prefix_len[i] + 1
        
        res = []
        for l, r in queries:
            l_len = prefix_len[l]
            r_len = prefix_len[r + 1]
            delta_sum = prefix_sum[r + 1] - prefix_sum[l]
            main_number = prefix_number[r + 1]
            sub_number = (prefix_number[l] * powers[r_len - l_len]) % MODULO
            delta_number = (main_number - sub_number) % MODULO
            res.append((delta_number * delta_sum) % MODULO)
        return res
