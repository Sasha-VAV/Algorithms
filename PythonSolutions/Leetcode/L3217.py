# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        root = ListNode(-1, head)
        curr = root
        while head:
            if head.val in nums:
                head = head.next
                continue
            curr.next = head
            curr = curr.next
            head = head.next
        if curr: curr.next = None
        return root.next

if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3)))
    Solution().modifiedList([2], a)