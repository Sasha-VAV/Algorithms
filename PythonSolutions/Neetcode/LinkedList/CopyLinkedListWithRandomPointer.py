from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = dict()
        tmp = head
        new_head = None
        while tmp is not None:
            nodes[tmp] = Node(tmp.val, tmp.next, tmp.random)
            if new_head is None:
                new_head = nodes[tmp]
            tmp = tmp.next
        tmp2 = head
        tmp = new_head
        while tmp is not None:
            tmp.next = nodes[nodes[tmp2].next] if nodes[tmp2].next is not None else None
            tmp.random = nodes[nodes[tmp2].random] if nodes[tmp2].random is not None else None
            tmp2 = tmp2.next
            tmp = tmp.next
        return new_head


if __name__ == '__main__':
    head = Node(1, random=None)
    head.next = Node(2, random=None)
    head.next.next = Node(3, random=None)
    head.next.random = head
    new_head = Solution().copyRandomList(head)
    new_head.val = -1
    pass