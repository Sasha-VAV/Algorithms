import random


class Node:
    def __init__(self, val, _next=None, bottom=None, c=1):
        self.val = val
        self.c = c
        self.next = _next
        self.bottom = bottom


class Skiplist:

    def __init__(self):
        self.head = None
        self.add(-1, True)

    def search(self, target: int) -> bool:
        if target < 0:
            return False
        if not self.head:
            return False
        def dfs(node):
            if node.val == target:
                return True
            if node.next and node.next.val <= target:
                return dfs(node.next)
            elif node.bottom:
                return dfs(node.bottom)
            return False
        return dfs(self.head)
    def add(self, num: int, f=False) -> None:
        if num < 0 and not f:
            return
        if not self.head:
            self.head = Node(num)
            return
        if self.head.next:
            self.head = Node(self.head.val, None, self.head)
        def dfs(node):
            if node.next and node.next.val <= num:
                return dfs(node.next)
            elif node.bottom and node.val != num:
                tmp = dfs(node.bottom)
                if tmp and random.random() < 0.5:
                    node.next = Node(num, node.next, tmp, tmp.c)
                    return node.next
                return None
            else:
                if node.bottom: dfs(node.bottom)
                if node.val == num:
                    node.c += 1
                    return node
                node.next = Node(num, node.next)
                return node.next
        dfs(self.head)

    def erase(self, num: int) -> bool:
        if num < 0:
            return False
        if not self.search(num):
            return False
        def dfs(node):
            if node.next and node.next.val <= num:
                dfs(node.next)
                if node.next.val == num:
                    if node.bottom: dfs(node.bottom)
                    if node.next.c == 1:
                        node.next = node.next.next
                    else:
                        node.next.c -= 1
                return
            elif node.bottom:
                dfs(node.bottom)
                return
            return
        dfs(self.head)
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

if __name__ == '__main__':
    sk = Skiplist()
    ref = []
    # Unlimited testcases
    while True:
        act = "ase"
        x = random.randint(0, len(act)-1)
        x = act[x]
        b = random.randint(0, 4)
        if x == "a":
            ref.append(b)
            sk.add(b)
        if x == "s":
            a = sk.search(b)
            assert (b in ref) == a
        if x == "e":
            if b not in ref:
                assert not sk.erase(b)
            else:
                ref.remove(b)
                assert sk.erase(b)
    pass