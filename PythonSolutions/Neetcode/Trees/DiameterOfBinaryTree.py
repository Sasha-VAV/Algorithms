from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_and_depth(root: Optional[TreeNode]) -> tuple[int, int]:
            if not root:
                return 0, 0
            l_diameter, l_depth = diameter_and_depth(root.left)
            r_diameter, r_depth = diameter_and_depth(root.right)
            return max(l_diameter, r_diameter, l_depth + r_depth), max(l_depth, r_depth) + 1
        return diameter_and_depth(root)[0]



if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    print(Solution().diameterOfBinaryTree(tree))