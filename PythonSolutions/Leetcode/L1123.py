from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_distance(self, root: Optional[TreeNode]) -> None:
        if root.left is None and root.right is None:
            root.lvl = 0
        else:
            if root.left is None:
                self.get_distance(root.right)
                root.lvl = 1 + root.right.lvl
            elif root.right is None:
                self.get_distance(root.left)
                root.lvl = 1 + root.left.lvl
            else:
                self.get_distance(root.left)
                self.get_distance(root.right)
                root.lvl = 1 + max(root.left.lvl, root.right.lvl)

    def lcaDeepestLeaves(self, root: Optional[TreeNode], do_distance=True) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if do_distance:
            self.get_distance(root)
        if root.left is None:
            return self.lcaDeepestLeaves(root.right, False)
        elif root.right is None:
            return self.lcaDeepestLeaves(root.left, False)
        left = root.left.lvl
        right = root.right.lvl
        if left > right:
            return self.lcaDeepestLeaves(root.left, False)
        elif right > left:
            return self.lcaDeepestLeaves(root.right, False)
        else:
            return root

