from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        heads = [None] * m
        for i, head in enumerate(lists):
            heads[i] = head
        arr = None
        while True:
            tmp = []
            for i, head in enumerate(heads):
                if head is not None:
                    tmp.append((i, head))
            if len(tmp) == 0:
                break
            tmp = min(tmp, key=lambda x: x[1].val)
            if arr is None:
                arr = tmp[1]
                tmp_arr = arr
            else:
                tmp_arr.next = tmp[1]
                tmp_arr = tmp_arr.next
            heads[tmp[0]] = heads[tmp[0]].next
        return arr


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(5)
    list3 = ListNode(3)
    list3.next = ListNode(6)
    Solution().mergeKLists([list1, list2, list3])