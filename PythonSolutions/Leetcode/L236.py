# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        seen = set()
        seen.add(p)
        seen.add(q)
        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            if l:
                return l
            r = dfs(node.right)
            if r:
                return r
            a = node.left in seen
            b = node.right in seen
            if a or b:
                if node in seen and (a or b):
                    return node
                if a and b:
                    return node
                seen.add(node)
            return None
        return dfs(root)