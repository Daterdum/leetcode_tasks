from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _is_lst1_greater_than_lst2(self, l1: ListNode, l2: ListNode):
        if not l1:
            return False

        if not l2:
            return True

        if l1.val > l2.val:
            return False

        else:
            return True

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n_1 = list1
        n_2 = list2

        head = node = ListNode()
        while n_1 or n_2:
            # print(f"\n{node.val=}")
            # print(n_1.val, n_2.val)
            if not n_1:
                node.next = n_2
                node = n_2
                n_2 = n_2.next

            elif not n_2:
                node.next = n_1
                node = n_1
                n_1 = n_1.next

            elif self._is_lst1_greater_than_lst2(n_1, n_2):
                node.next = n_1
                node = n_1
                n_1 = n_1.next

            else:
                node.next = n_2
                node = n_2
                n_2 = n_2.next

        return head.next
