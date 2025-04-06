from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        k = 0
        while tmp is not None:
            k += 1
            tmp = tmp.next
        tmp = head
        n = k - n
        k = 0
        if n == 0:
            head = head.next
            return head
        while k < n:
            prev = tmp
            tmp = tmp.next
            k += 1
        tmp = tmp.next
        prev.next = tmp
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(Solution().removeNthFromEnd(head, 2))