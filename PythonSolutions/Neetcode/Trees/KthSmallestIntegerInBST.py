from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_nodes(root):
            if not root:
                return []
            return find_nodes(root.left) + [root.val] + find_nodes(root.right)
        nodes = find_nodes(root)
        return nodes[k-1]


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    print(Solution().kthSmallest(tree, 2))