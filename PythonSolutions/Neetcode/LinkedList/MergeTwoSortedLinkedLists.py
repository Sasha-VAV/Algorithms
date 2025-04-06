from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                merged_list = list1
                list1 = list1.next
            else:
                merged_list = list2
                list2 = list2.next
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2
        else:
            return None
        tmp_head = merged_list
        while list1 and list2:
            if list1.val <= list2.val:
                tmp_head.next = list1
                tmp_head = tmp_head.next
                list1 = list1.next
            else:
                tmp_head.next = list2
                tmp_head = tmp_head.next
                list2 = list2.next
        if list1:
            tmp_head.next = list1
        if list2:
            tmp_head.next = list2
        return merged_list


if __name__ == '__main__':
    a = ListNode(5)
    a = ListNode(3, a)
    a = ListNode(1, a)
    b = ListNode(6)
    b = ListNode(4, b)
    b = ListNode(2, b)
    print(Solution().mergeTwoLists(a, b))

