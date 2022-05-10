class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        p = head
        while p.next:
            if p.child is None:
                p = p.next
                continue

            temp = p.child
            while temp.next:
                temp = temp.next

            temp.next = p.next
            if p.next:
                p.next.prev = temp

            p.next = p.child
            p.child.prev = p
            p.child = None

        return head


