# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find len of this list
        slow = head
        fast = head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is last in the first half
        curr = slow.next
        # Splitting
        slow.next = None
        # reversing
        second_head = None
        while curr:
            tmp = curr.next
            curr.next = second_head
            second_head = curr

            curr = tmp
        res = 0
        while head and second_head:
            res = max(res, head.val + second_head.val)
            head = head.next
            second_head = second_head.next
        return res