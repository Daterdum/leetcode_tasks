import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _validate(self, node: Optional[TreeNode], min_: int, max_: int):
        if not node:
            return True

        if node.val <= min_ or node.val >= max_:
            return False

        return self._validate(node.left, min_, node.val) and self._validate(node.right, node.val, max_)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self._validate(root, max_=math.inf, min_=-math.inf)
