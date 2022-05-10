from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode], index=0) -> Optional[ListNode]:
        if not head:
            return -1

        try:
            if getattr(head.next, 'marked'):
                return head.next

        except AttributeError as err:
            pass

        head.__setattr__('marked', True)

        return self.detectCycle(head.next, index + 1)