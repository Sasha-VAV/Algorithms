from collections import deque
from typing import Optional
from functools import cache
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return l + r + node.val
        total = dfs(root)
        q = deque([root])
        best_dif = total
        a, b = total, 0
        while q:
            node = q.pop()
            curr = dfs(node)
            if abs(total - 2*curr) < best_dif:
                best_dif = abs(total - 2*curr)
                a, b = total - curr, curr
            if node.left: q.appendleft(node.left)
            if node.right: q.appendleft(node.right)
        mod = 10**9 + 7
        return (a % mod) * (b % mod) % mod