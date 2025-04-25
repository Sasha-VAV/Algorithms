class Solution:
    def myAtoi(self, s: str) -> int:
        is_neg = False
        numbers = []
        state = 0
        for c in s:
            if state == 0 and c == " ":
                continue
            if state == 0 and (c == "-" or c == "+"):
                is_neg = c == "-"
                state = 1
                continue
            if c.isdigit():
                state = 1
                numbers.append(int(c))
                continue
            break
        res = 0
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        for number in numbers:
            res *= 10
            res += number
            if res > (max_int + 1):
                break
        if is_neg and res > (max_int + 1):
            return min_int
        if not is_neg and res > max_int:
            return max_int
        if is_neg:
            return res * -1
        return res
