from typing import List, Optional
from copy import deepcopy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def clone(self, root):
        if root is None:
            return None
        node = TreeNode(root.val)
        node.left = self.clone(root.left)
        node.right = self.clone(root.right)
        return node

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = dict()
        def create(k):
            if k % 2 == 0:
                return []
            if k in cache:
                return [self.clone(x) for x in cache[k]]
            if k == 1:
                cache[k] = [TreeNode()]
                return [TreeNode()]
            res = []
            for i in range(1, k, 2):
                left = create(i)
                right = create(k - i - 1)
                for l in left:
                    for r in right:
                        res.append(TreeNode(0, l, r))
            cache[k] = res
            return res
        return create(n)