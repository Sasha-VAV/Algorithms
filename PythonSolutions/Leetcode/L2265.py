# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            curr_sum = node.val
            curr_count = 1
            for sub in (node.left, node.right):
                if sub is None: 
                    continue
                a, b = dfs(sub)
                curr_sum += a
                curr_count += b
            if node.val == (curr_sum // curr_count):
                res += 1
            return curr_sum, curr_count
        dfs(root)
        return res
