# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def to_list(root):
            if not root:
                return []
            return to_list(root.left) + [root.val] + to_list(root.right)

        arr1 = to_list(root1)
        arr2 = to_list(root2)
        n = len(arr1)
        m = len(arr2)
        i = 0
        j = 0
        res = []
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        return res
