from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        heap = []
        lookup = dict()
        for i, node in enumerate(lists):
            if not node: continue
            heapq.heappush(heap, (node.val, i))
            lookup[i] = node
        res = None
        sub = None
        while heap:
            _, i = heapq.heappop(heap)
            node = lookup[i]
            if not res:
                res = ListNode(node.val)
                sub = res
            sub.next = ListNode(node.val)
            sub = sub.next
            sub.next = None
            if node.next:
                heapq.heappush(heap, (node.next.val, i))
                lookup[i] = node.next
        if res: return res.next
        return None