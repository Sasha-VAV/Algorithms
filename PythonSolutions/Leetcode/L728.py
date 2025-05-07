from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            a = i
            while a > 0:
                if a % 10 == 0 or i % (a % 10) != 0:
                    break
                a //= 10
            else:
                res.append(i)
        return res


if __name__ == '__main__':
    print(Solution().selfDividingNumbers(1, 22))