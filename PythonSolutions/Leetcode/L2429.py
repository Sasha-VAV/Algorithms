class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = bin(num2).count('1')
        num1 = list(bin(num1)[2:])
        for i, c in enumerate(num1):
            if c == '1':
                num1[i] = '2'
                count -= 1
            if count == 0:
                break
        else:
            i = len(num1) - 1
            while count != 0 and i > -1:
                if num1[i] != '2':
                    num1[i] = '2'
                    count -= 1
                i -= 1
            if i == -1 and count != 0:
                num1 = ['2'] * count + num1
        return int(''.join('1' if c == '2' else '0' for c in num1), 2)


if __name__ == '__main__':
    print(Solution().minimizeXor(num1=1, num2=12))