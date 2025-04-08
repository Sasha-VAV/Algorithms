from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS solution
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         right_arr = self.rightSideView(root.right)
#         left_arr = self.rightSideView(root.left)
#         if len(right_arr) >= len(left_arr):
#             return [root.val] + right_arr
#         for i, right in enumerate(right_arr):
#             left_arr[i] = right
#         return [root.val] + left_arr


# BFS solution
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr.val)
        return res


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    print(Solution().rightSideView(tree))