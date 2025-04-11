from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            mid = indices[root.val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(preorder) - 1)


if __name__ == '__main__':
    preorder = [1,2,4,5,3,6,7,8]
    inorder = [4,2,5,1,6,3,7,8]
    root = Solution().buildTree(preorder, inorder)
    pass
