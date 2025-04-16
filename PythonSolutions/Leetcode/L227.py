from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        d = deque()
        def find_next_op(string, idx=0):
            res = string.find("+", idx)
            tmp = string.find("-", idx)
            res = tmp if -1 < tmp < res or res == -1 else res
            tmp = string.find("*", idx)
            res = tmp if -1 < tmp < res or res == -1 else res
            tmp = string.find("/", idx)
            res = tmp if -1 < tmp < res or res == -1 else res
            return res
        i = 0
        j = -2
        while j != 0:
            j = find_next_op(s, i)
            j = 0 if j == -1 else j
            x = int(s[i:j]) if j else int(s[i:])
            if d and (d[-1] == "*" or d[-1] == "/"):
                op = d.pop()
                y = d.pop()
                if op == "*":
                    d.append(y * x)
                else:
                    d.append(y // x)
            else:
                d.append(x)
            if j != 0:
                d.append(s[j])
            i = j + 1
        x = d.popleft()
        while d:
            op = d.popleft()
            y = d.popleft()
            x = x - y if op == "-" else y + x
        return x


if __name__ == '__main__':
    print(Solution().calculate("1-1+1"))