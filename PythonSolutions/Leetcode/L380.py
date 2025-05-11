import random

class RandomizedSet:

    def __init__(self):
        self.dict = dict()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        idx = self.dict.get(val, -1)
        if idx == -1:
            return False
        self.dict[self.list[-1]] = idx
        self.list[idx] = self.list[-1]
        self.list.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        x = int(random.random() * len(self.list))
        return self.list[x]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()