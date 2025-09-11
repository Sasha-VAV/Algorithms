class Solution:
    def sortVowels(self, s: str) -> str:
        letters = {
            "A": 0,
            "E": 0,
            "I": 0,
            "O": 0,
            "U": 0,
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0,
        }
        arr = []
        for i in s:
            if i in letters:
                arr.append("_")
                letters[i] += 1
            else:
                arr.append(i)
        new_letters = {}
        for k, v in letters.items():
            if v == 0: continue
            new_letters[k] = v
        letters = new_letters
        for i, x in enumerate(arr):
            if x != "_": continue
            k, v = next(iter(letters.items()))
            letters[k] -= 1
            if letters[k] == 0:
                letters.pop(k)
            arr[i] = k
        return "".join(arr)
