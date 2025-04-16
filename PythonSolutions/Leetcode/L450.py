# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        def get_node(node, key):
            nonlocal parent
            if not node:
                return None
            if node.val == key:
                return node
            if node.val > key:
                parent = node
                return get_node(node.left, key)
            parent = node
            return get_node(node.right, key)
        node = get_node(root, key)
        if not node:
            return root
        if not node.right:
            node = node.left
        else:
            left = node.left
            node = node.right
            tmp = node
            while tmp.left:
                tmp = tmp.left
            tmp.left = left
        if parent and parent.val > key:
            parent.left = node
        elif parent:
            parent.right = node
        else:
            return node
        return root