# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        roots = set()
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
                roots.add(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if child in roots:
                roots.remove(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        if len(roots) != 1:
            raise ValueError("We have multiple trees")
        root = list(roots)[0]
        return nodes[root]