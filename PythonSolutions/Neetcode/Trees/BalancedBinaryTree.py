from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0, 0
            l_h, l_b = get_height(node.left)
            r_h, r_b = get_height(node.right)
            return max(l_h, r_h) + 1, min(l_b, r_b, max(1 - abs(l_h - r_h), -1))
        return get_height(root)[1] != -1


if __name__ == "__main__":
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    print(Solution().isBalanced(tree))