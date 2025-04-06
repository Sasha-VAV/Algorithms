class LRUCache:
    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.kv = dict()
        self.head = None
        self.tail = None

    def update_node(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.next
            self.tail.prev = None
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = self.head
        self.head.next = node
        self.head = node
        pass

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        node = self.kv[key]
        if self.len > 1:
            self.update_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            node = self.kv[key]
            node.val = value
            if self.len > 1:
                self.update_node(node)
            return
        self.len += 1
        node = self.Node(key, value, prev=self.head)
        self.kv[key] = node
        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.head.next = node
        self.head = self.head.next
        self.head.next = None
        if self.len > self.capacity:
            self.kv.pop(self.tail.key)
            self.tail = self.tail.next
            self.tail.prev = None
            self.len -= 1



if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.get(1)
    lru.get(2)
    lru.get(4)
    lru.put(4, 4)
    lru.get(1)
    lru.get(2)
    lru.get(3)
    lru.get(4)
    lru.get(2)
    lru.put(1, 8)
    lru.put(3, 7)
    lru.get(1)
    lru.get(2)
    lru.get(3)
    lru.get(4)
    lru.get(5)
    lru.get(2)
    lru.get(3)
    lru.get(4)
    lru.put(1, 9)
    lru.put(6,6)
    pass
