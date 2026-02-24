# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        powers = [1]
        for _ in range(32):
            powers.append(powers[-1] * 2)
        def dfs(node, values):
            nonlocal res
            if not node:
                return
            curr = values + [node.val]
            if not node.left and not node.right:
                for i, value in enumerate(reversed(curr)):
                    res += value * powers[i]
                return
            dfs(node.left, curr)
            dfs(node.right, curr)
        dfs(root, [])
        return res