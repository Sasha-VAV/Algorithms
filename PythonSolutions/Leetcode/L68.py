from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        level = []
        x = -1
        for word in words:
            if x + len(word) + 1 > maxWidth:
                r = ""
                if len(level) > 1:
                    a = (maxWidth - x) // (len(level) - 1) + 1
                    b = (maxWidth - x) % (len(level) - 1)
                else:
                    a = 0
                    b = 0
                r += level[0]
                for l in level[1:]:
                    r += " " * a + " " * min(b, 1) + l
                    b -= 1
                r += " " * (maxWidth - len(r))
                res.append(r)
                x = -1
                level.clear()
            x += len(word) + 1
            level.append(word)
        if level:
            r = level[0]
            for l in level[1:]:
                r += " " + l
            r += " " * (maxWidth - len(r))
            res.append(r)
        return res


if __name__ == '__main__':
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print("\n".join(Solution().fullJustify(words, maxWidth)))