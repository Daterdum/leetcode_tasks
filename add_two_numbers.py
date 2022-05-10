from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], extra: int = 0) -> Optional[ListNode]:
        val = l1.val + l2.val + extra

        if not (l1.next or l2.next):
            if val < 10:
                return ListNode(
                    val=val,
                    next=None
                )

        return ListNode(
            val=val % 10,
            next=self.addTwoNumbers(
                l1.next if l1.next else ListNode(val=0, next=None),
                l2.next if l2.next else ListNode(val=0, next=None),
                val // 10)
        )
