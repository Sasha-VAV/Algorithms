class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sorted_positions = sorted((x, i) for i, x in enumerate(positions))
        stack = deque()
        res = []
        for _, i in sorted_positions:
            health = healths[i]
            direction = directions[i]
            if direction == "R":
                stack.append([health, i])
                continue
            while stack and stack[-1][0] < health:
                stack.pop()
                health -= 1
            if stack:
                if stack[-1][0] == health:
                    stack.pop()
                else:
                    stack[-1][0] -= 1
            else:
                res.append((health, i))
        while stack:
            res.append(stack.pop())
        res.sort(key=lambda x: x[1])
        return [x[0] for x in res]