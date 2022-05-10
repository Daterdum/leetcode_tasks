from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _print(node: ListNode):
    while node.next:
        print(f"{node.val=} {node.next.val=}")
        node = node.next

    print(f"{node.val=} {None}")



class Solution:

    def _len(self, head: ListNode) -> int:
        node = head
        counter = 1
        while node.next:
            counter += 1
            node = node.next

        return counter

    def _rotate_once(self, head: ListNode) -> ListNode:
        node = head
        prev_node = None

        while node.next:
            # print(node.val, node.next.val)

            prev_node = node
            node = node.next

        else:
            node.next = head
            prev_node.next = None

            return node

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        print("\nRotating")
        if not head:
            return None

        if head.next is None:
            return head

        if (lst_len := self._len(head)) < k:

            k %= lst_len

        print(f"{lst_len=}")
        print(f"{k=}")

        node = head

        for _ in range(k):
            node = self._rotate_once(head=node)

        _print(node)

        return node
