# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        del_list = set(to_delete)

        def del_node(node):
            if not node: return [None]
            left = del_node(node.left)
            right = del_node(node.right)
            node.left = left[0]
            node.right = right[0]
            arr = [None] if node.val in del_list else [node]
            if arr[0] == None:
                arr.extend(left)
                arr.extend(right)
            else:
                arr.extend(left[1:])
                arr.extend(right[1:])
            return arr

        res = []
        for x in del_node(root):
            if x: res.append(x)
        return res

