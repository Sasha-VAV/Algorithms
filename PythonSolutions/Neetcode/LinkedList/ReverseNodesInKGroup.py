from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        tmp = head
        i = 0
        prev_group = None
        curr_group = None
        prev = head
        while tmp is not None:
            if i > 0 and i % k == 0:
                if prev_group is None:
                    prev.next = tmp
                    head = curr_group
                    curr_group = None
                else:
                    prev.next = tmp
                    prev_group.next = curr_group
                    curr_group = None
                prev_group = prev
                prev = prev.next
            tmp2 = curr_group
            curr_group = tmp
            tmp = tmp.next
            curr_group.next = tmp2
            i += 1
        if i > 0 and i % k == 0:
            if prev_group is None:
                prev.next = tmp
                head = curr_group
            else:
                prev_group.next = curr_group
        else:
            c = None
            a = curr_group
            while a is not None:
                b = c
                c = a
                a = a.next
                c.next = b
            prev_group.next = c
        return head


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    Solution().reverseKGroup(head, 3)