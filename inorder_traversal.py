from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _recursive_traversal(self, node, lst):
        if node:
            self._recursive_traversal(node.left, lst)
            lst.append(node.val)
            self._recursive_traversal(node.right, lst)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self._recursive_traversal(root, lst)
        return lst
