# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        
        from_start = (n - k) % n
        if not from_start:
            return head

        end = curr
        curr = head
        for _ in range(from_start - 1):
            curr = curr.next
        end.next = head
        head = curr.next
        curr.next = None
        return head
        