from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=-1001, max_val=1001) -> bool:
        if not root:
            return True
        if root.left and not min_val < root.left.val < root.val < max_val:
            return False
        if root.right and not min_val < root.val < root.right.val < max_val:
            return False
        return (self.isValidBST(root.left, min_val=min_val, max_val=root.val)
                and self.isValidBST(root.right, min_val=root.val, max_val=max_val))


if __name__ == "__main__":
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().isValidBST(tree))