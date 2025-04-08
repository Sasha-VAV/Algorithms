from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, max_val = -101) -> int:
        if not root:
            return 0
        res = root.val >= max_val
        res += self.goodNodes(root.left, max(max_val, root.val))
        res += self.goodNodes(root.right, max(max_val, root.val))
        return res


if __name__ == '__main__':
    t = TreeNode(5)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    print(Solution().goodNodes(t))