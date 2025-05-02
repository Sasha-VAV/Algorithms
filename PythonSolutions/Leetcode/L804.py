class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            arr = []
            for c in word:
                arr.append(chars[ord(c)-ord('a')])
            res.add(''.join(arr))
        return len(res)
