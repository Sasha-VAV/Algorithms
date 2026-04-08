class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        direction = 0
        mapping = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0),
        }
        res = 0
        x, y = (0, 0)
        for command in commands:
            if command == -1:
                direction += 1
                direction %= 4
                continue
            if command == -2:
                direction -= 1
                direction %= 4
                continue
            x_shift, y_shift = mapping[direction]
            while command:
                if (x + x_shift, y + y_shift) in obstacles:
                    break
                x += x_shift
                y += y_shift
                command -= 1
                res = max(res, x**2 + y**2)
        return res