from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_q = deque([root])
        q = deque()
        lowest_trees = deque()
        while q or new_q:
            if not q:
                q = new_q
                lowest_trees = q.copy()
                new_q = deque()
            node = q.pop()
            if node.left: new_q.appendleft(node.left)
            if node.right: new_q.appendleft(node.right)
        lowest_trees = set(lowest_trees)
        def dfs(node):
            if not node: return set()
            l = dfs(node.left)
            r = dfs(node.right)
            if not isinstance(l, set): return l
            if not isinstance(r, set): return r
            curr = {x for x in (l | r | {node}) if x in lowest_trees}
            if len(curr) == len(lowest_trees):
                return node
            return curr
        return dfs(root)


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    print(Solution().subtreeWithAllDeepest(tree))