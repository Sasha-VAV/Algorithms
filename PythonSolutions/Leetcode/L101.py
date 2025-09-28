from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.appendleft(root)
        new_q: List[TreeNode] = list()
        while q or new_q:
            if not q:
                for i in range(len(new_q) // 2):
                    if new_q[i] is None and new_q[len(new_q) - i - 1] is None: continue
                    if new_q[i] is None or new_q[len(new_q) - i - 1] is None: return False
                    if new_q[i].val != new_q[len(new_q) - i - 1].val: return False
                for x in new_q:
                    if x is not None: q.appendleft(x)
                new_q.clear()
            if not q: break
            node = q.pop()
            new_q.append(node.left)
            new_q.append(node.right)
        return True