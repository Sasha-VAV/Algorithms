class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = []
        force = 0
        state = 0
        for c in dominoes:
            if c == 'R':
                if force > 0:
                    if state == 0:
                        res.append('.'*force)
                    else:
                        res.append('R'*force)
                force = 0
                state = 1
                res.append(c)
            elif c == 'L' and state == 1:
                res.append('R'*(force//2))
                if force % 2 == 1:
                    res.append('.')
                res.append(c*(force//2+1))
                force = 0
                state = 0
            elif c == 'L' and state == 0:
                res.append(c*(force+1))
                force = 0
            else:
                force += 1
        if force > 0:
            if state == 0:
                res.append('.'*force)
            else:
                res.append('R'*force)
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().pushDominoes("R.R.L"))