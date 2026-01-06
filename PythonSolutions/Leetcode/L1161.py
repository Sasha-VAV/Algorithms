# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        new_q = deque()
        curr = 0
        curr_idx = 1
        max_sum = float('-inf')
        max_idx = 1
        while q or new_q:
            if not q:
                if curr > max_sum:
                    max_sum = curr
                    max_idx = curr_idx
                q = new_q
                new_q = deque()
                curr = 0
                curr_idx += 1
            node = q.pop()
            if not node: continue
            curr += node.val
            new_q.appendleft(node.left)
            new_q.appendleft(node.right)
        return max_idx