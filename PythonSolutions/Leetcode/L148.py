# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None
        left = self.sortList(left)
        right = self.sortList(right)

        res = ListNode()
        curr = res
        while left or right:
            if not left:
                curr.next = right
                right = right.next
            elif not right:
                curr.next = left
                left = left.next
            else:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
            curr = curr.next
        return res.next