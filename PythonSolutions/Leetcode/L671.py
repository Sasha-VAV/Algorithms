import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        heap = []
        keys = set()
        def dfs(node):
            nonlocal heap
            if not node:
                return
            if (len(heap) < 2 or -heap[0] > node.val) and node.val not in keys:
                heapq.heappush(heap, -node.val)
                keys.add(node.val)
            if len(heap) > 2:
                keys.remove(-heapq.heappop(heap))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return -1 if len(heap) < 2 else -heap[0]