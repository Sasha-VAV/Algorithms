# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        tmp1 = head
        tmp2 = head.next
        while tmp1 and tmp2:
            if tmp1 == tmp2:
                return True
            tmp1 = tmp1.next
            tmp2 = tmp2.next.next if tmp2.next else None
        return False