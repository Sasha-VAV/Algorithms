from collections import deque
from typing import List, Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        q = deque()
        q.append(root)
        level = deque()
        isrl = True
        while q:
            node = q.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            if not q and level:
                if isrl:
                    res.append([node.val for node in level][::-1])
                else:
                    res.append([node.val for node in level])
                q = level.copy()
                level.clear()
                isrl = not isrl
        return res


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    tree.left.right.left = TreeNode(10)
    tree.left.right.right = TreeNode(11)
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)
    print(Solution().zigzagLevelOrder(tree))