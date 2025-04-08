from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        left_arr = self.levelOrder(root.left) if root.left else []
        right_arr = self.levelOrder(root.right) if root.right else []
        if len(left_arr) >= len(right_arr):
            for i, val in enumerate(right_arr):
                left_arr[i].extend(val)
            left_arr.insert(0, [root.val])
            return left_arr
        else:
            for i, val in enumerate(left_arr):
                right_arr[i][:0] = val
            right_arr.insert(0, [root.val])
            return right_arr


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    print(Solution().levelOrder(tree))