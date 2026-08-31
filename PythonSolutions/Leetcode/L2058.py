# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        first_critical = None
        prev_critical = None
        res = [None, None]

        def is_critical(a, b, c):
            return a > b and b < c or a < b and b > c
        idx = 0
        while head and head.next:
            if prev is not None and is_critical(prev, head.val, head.next.val):
                if first_critical is None:
                    first_critical = idx
                if prev_critical is not None:
                    diff = idx - prev_critical
                    max_diff = idx - first_critical
                    res[0] = diff if res[0] is None else min(diff, res[0])
                    res[1] = diff if res[1] is None else max(max_diff, res[1])
                prev_critical = idx
            prev = head.val
            head = head.next
            idx += 1
        if res[0] is None:
            return [-1, -1]
        return res