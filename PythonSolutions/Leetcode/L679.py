from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = 4
        cache = dict()
        def search(arr):
            if arr in cache:
                return cache[arr]
            if len(arr) == 1:
                cache[arr] = round(arr[0], 5) == 24
                return cache[arr]
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    a, b = arr[i], arr[j]
                    new_arr = arr[:i] + arr[i+1:j] + arr[j+1:]
                    for _ in range(2):
                        for k in "+-*/":
                            try:
                                if search(new_arr + (eval(str(a) + k + str(b)),)):
                                    cache[arr] = True
                                    return True
                            except Exception as e:
                                continue
                        a, b = b, a
            cache[arr] = False
            return False
        return search(tuple(cards))