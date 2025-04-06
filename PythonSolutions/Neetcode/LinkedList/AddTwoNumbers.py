from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        tmp = head
        add = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 is not None or l2 is not None or add != 0:
            curr = add
            if l1 is not None:
                curr += l1.val
                l1 = l1.next
            if l2 is not None:
                curr += l2.val
                l2 = l2.next
            add = curr // 10
            curr %= 10
            tmp.next = ListNode(curr)
            tmp = tmp.next
        return head


if __name__ == '__main__':
    a = ListNode(9)
    b = ListNode(9)
    print(Solution().addTwoNumbers(a, b))

