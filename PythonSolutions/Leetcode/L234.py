from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        tmp = head
        i = 0
        while i < (n + 1) // 2:
            tmp = tmp.next
            i += 1
        half = None
        while i < n:
            a = half
            half = tmp
            tmp = tmp.next
            half.next = a
            i += 1
        while half:
            if head.val != half.val:
                return False
            head = head.next
            half = half.next
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))