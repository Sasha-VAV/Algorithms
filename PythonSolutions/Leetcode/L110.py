# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lvl):
            if not node:
                return lvl - 1, True
            l = dfs(node.left, lvl + 1)
            if not l[1]: return -1, False
            r = dfs(node.right, lvl + 1)
            if not r[1]: return -1, False
            if abs(l[0] - r[0]) > 1: return -1, False
            return max(l[0], r[0]), True
        return dfs(root, 0)[1]