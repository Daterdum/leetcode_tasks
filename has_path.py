from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _recursive_traversal(self, node, target_sum, current_sum) -> bool:
        if node:
            self._recursive_traversal(node.left, current_sum)
            current_sum.append(node.val)
            self._recursive_traversal(node.right, current_sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._recursive_traversal(
            root.left,
            targetSum,
            root.val
        ) or self._recursive_traversal(
            root.right,
            targetSum,
            root.val
        )


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        elif not root.left and not root.right:
            if root.val == targetSum:
                return True

        targetSum -= root.val

        return self.hasPathSum(
            root.left,
            targetSum,
        ) or self.hasPathSum(
            root.right,
            targetSum,
        )
