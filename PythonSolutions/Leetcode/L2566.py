class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        min_num = int(num.replace(num[0], "0"))
        i = 0
        while i < len(num) and num[i] == "9":
            i += 1
        if i < len(num):
            max_num = int(num.replace(num[i], "9"))
        else:
            max_num = int(num)
        return max_num - min_num