from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_mirror_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        elif p and q:
            if p.val == q.val:
                return self.is_mirror_tree(p.left, q.right) and self.is_mirror_tree(p.right, q.left)

        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror_tree(root.left, root.right)
