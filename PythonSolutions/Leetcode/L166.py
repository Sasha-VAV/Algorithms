from collections import OrderedDict


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0: return str(numerator//denominator)
        mem = OrderedDict()
        res = []
        if (numerator > 0) == (denominator < 0): res.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += [str(numerator // denominator), "."]
        numerator %= denominator
        numerator *= 10
        while True:
            if numerator == 0: break
            if numerator in mem: break
            mem[numerator] = numerator // denominator
            numerator %= denominator
            numerator *= 10
        for k, v in mem.items():
            if k == numerator: res.append("(")
            res.append(str(v))
        if "(" in res: res.append(")")
        return "".join(res)




if __name__ == '__main__':
    print(Solution().fractionToDecimal(-50, 8))