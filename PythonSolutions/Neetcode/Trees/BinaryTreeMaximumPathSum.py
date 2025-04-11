from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> tuple[int, int]:
            if node.left is None and node.right is None:
                return node.val, node.val
            if node.left is None or node.right is None:
                a = dfs(node.left) if node.left is not None else dfs(node.right)
                continuable_max = max(a[1], 0) + node.val
                node_max = max(a[0], continuable_max)
                return node_max, continuable_max
            a = dfs(node.left)
            b = dfs(node.right)
            continuable_max = max(a[1], b[1], 0) + node.val
            node_max = max(a[0], b[0], a[1] + b[1] + node.val, continuable_max)
            return node_max, continuable_max
        return dfs(root)[0]


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    print(Solution().maxPathSum(t))