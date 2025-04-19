from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_sum = max(max_sum, node.val + left + right, node.val, node.val + max(left, right))
            return node.val + max(left, right, 0)
        dfs(root)
        return max_sum


if __name__ == '__main__':
    t = TreeNode(2)
    t.left = TreeNode(-1)

    print(Solution().maxPathSum(t))