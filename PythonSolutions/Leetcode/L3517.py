class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = [0] * 26
        a_ord = ord("a")
        for c in s:
            counter[ord(c) - a_ord] += 1
        res = []
        middle_char = None
        for i in range(26):
            if counter[i] % 2 == 1:
                middle_char = chr(i + a_ord)
            res.append(chr(i + a_ord) * (counter[i] // 2))
        if middle_char is not None:
            res.append(middle_char)
        for i in range(25, -1, -1):
            res.append(chr(i + a_ord) * (counter[i] // 2))

        return "".join(res)