# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()

        def dfs(node):
            nonlocal counter
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            curr = l + r + node.val
            counter[curr] += 1
            return curr
        
        dfs(root)

        max_value = counter.most_common(1)[0][1]
        return [k for k, v in counter.items() if v == max_value]