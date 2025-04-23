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
        if node == self.end:
            return
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.prev = self.end
        self.end.next = node
        self.end = self.end.next
        if node.key in self.kv:
            self.kv.pop(node.key)
        if node == self.start or len(self.kv) == self.capacity:
            if self.start.key in self.kv:
                self.kv.pop(self.start.key)
            self.start = self.start.next
            self.start.prev = None
        node.next = None
        self.kv[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        node = self.kv[key]
        self.push_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.kv:
            node = self.Node(key, value)
        else:
            node = self.kv[key]
            node.val = value
        if self.start is None:
            self.start = node
            self.end = node
            self.kv[key] = node
        else:
            self.push_node(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    print(lru.get(2))
    lru.put(1, 1)
    lru.put(4, 1)
    print(lru.get(2))
