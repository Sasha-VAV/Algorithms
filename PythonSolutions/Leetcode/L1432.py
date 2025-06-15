class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        i = 0
        while i < len(num) and num[i] == "9":
            i += 1
        if i < len(num):
            a = num.replace(num[i], "9")
        else:
            a = num
        i = 0
        while i < len(num) and num[i] in "10":
            i += 1
        if i < len(num):
            if i == 0:
                b = num.replace(num[i], "1")
            else:
                b = num.replace(num[i], "0")
        else:
            b = num
        return int(a) - int(b)