from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            n += 1
        tmp = head
        prev = None
        for i in range(n):
            if i == (n - 1) // 2:
                reversed_head = tmp.next
                tmp.next = None
                tmp = head
                tmp2 = reversed_head
            elif i < (n - 1) // 2:
                tmp = tmp.next
            else:
                reversed_head = tmp2
                tmp2 = tmp2.next
                reversed_head.next = prev
                prev = reversed_head
        tmp = head
        for i in range(n // 2):
            tmp1 = tmp.next
            tmp.next = reversed_head
            tmp = tmp.next
            reversed_head = reversed_head.next
            tmp.next = tmp1
            tmp = tmp.next



if __name__ == '__main__':
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)
    print(Solution().reorderList(head))

