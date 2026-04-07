class Robot:

    def __init__(self, width: int, height: int):
        self.perimeter = 2 * width + 2 * height - 4
        self.width = width
        self.height = height
        self.pos = 0
        self.calls = 0
        self.thresholds = [
            self.width - 1, # East
            self.width + self.height - 2, # North
            2 * self.width + self.height - 3, # West,
        ]

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %= self.perimeter
        self.calls += 1

    def getPos(self) -> List[int]:
        if self.pos <= self.thresholds[0]:
            return [self.pos, 0]
        if self.pos <= self.thresholds[1]:
            return [self.thresholds[0], self.pos - self.thresholds[0]]
        if self.pos <= self.thresholds[2]:
            return [self.thresholds[2] - self.pos, self.height - 1]
        return [0, self.perimeter - self.pos]

    def getDir(self) -> str:
        if self.pos == 0 and self.calls:
            return "South"
        if self.pos <= self.thresholds[0]:
            return "East"
        if self.pos <= self.thresholds[1]:
            return "North"
        if self.pos <= self.thresholds[2]:
            return "West"
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()