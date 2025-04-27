from typing import List, Optional
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        def flatten(head):
            while head.next:
                if head.child is None:
                    head = head.next
                    continue
                child = head.child
                a = head.next
                head.next = child
                child.prev = head
                b = flatten(child)
                b.next = a
                a.prev = b
                head.child = None
                head = a
            if head.child:
                head.next = head.child
                head.child.prev = head
                b = flatten(head.child)
                head.child = None
                head = b
            return head
        flatten(head)
        return head



if __name__ == '__main__':
    head = Node(3, None, None, None)
    head = Node(2, None, None, head)
    head = Node(1, None, None, head)
    head = Solution().flatten(head)
    pass