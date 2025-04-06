from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = head
        b = head.next
        while a and b and a != b:
            if not a.next or not b.next or not b.next.next:
                return False
            a = a.next
            b = b.next.next
        if a and b and a == b:
            return True
        return False


if __name__ == '__main__':
    a = ListNode(1)
    a = ListNode(2, a)
    a = ListNode(3, a)
    a = ListNode(4, a)
    a = ListNode(5, a)
    a.next.next.next = a
    print(Solution().hasCycle(a))