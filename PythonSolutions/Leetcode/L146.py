class LRUCache:
    class Node:
        def __init__(self, key, val, prev=None, _next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = _next

    def __init__(self, capacity: int):
        self.start = None
        self.end = None
        self.kv = dict()
        self.capacity = capacity

    def push_node(self, node):
        node.prev = self.end
        self.end.next = node
        self.end = self.end.next
        if len(self.kv) > self.capacity or node == self.start:
            self.kv.pop(self.start.key)
            self.start = self.start.next
            self.start.prev = None
        self.end.next = None
        self.kv[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self.push_node(self.kv[key])
        return self.kv[key].val

    def put(self, key: int, value: int) -> None:
        if self.start is None:
            self.start = self.end = self.Node(key, value)
            self.kv[key] = self.start
        else:
            self.push_node(self.Node(key, value))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    print(lru.get(1))
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
