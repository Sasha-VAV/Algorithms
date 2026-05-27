class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ref = [0] * 26 # states
        a_num = ord('a')
        for c in word:
            ref_num = ord(c.lower()) - a_num
            match ref[ref_num]:
                case 0:
                    if c.isupper():
                        ref[ref_num] = -1
                    else:
                        ref[ref_num] = 1
                case 1:
                    if c.isupper():
                        ref[ref_num] = 2
                case 2:
                    if c.islower():
                        ref[ref_num] = -1
        
        res = 0
        for v in ref:
            if v == 2:
                res += 1
        return res