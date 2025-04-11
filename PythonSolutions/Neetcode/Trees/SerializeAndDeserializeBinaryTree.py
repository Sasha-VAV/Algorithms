from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        def dfs(node):
            nonlocal res
            res += str(node.val)
            if node.left:
                res += "L"
                dfs(node.left)
            if node.right:
                res += "R"
                dfs(node.right)
            res += "U"
            return
        dfs(root)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        def find_first_op(string: str, start_idx=0) -> int:
            ops = [string.find("L", start_idx), string.find("R", start_idx), string.find("U", start_idx)]
            return min(max(ops), min(ops, key=lambda x: x if x >= 0 else 10000000))
        idx = find_first_op(data)
        if idx == -1:
            return TreeNode(int(data))
        root = TreeNode(int(data[:idx]))
        def dfs(node):
            nonlocal idx
            if not -1 < idx < len(data):
                return node
            if data[idx] == "U":
                idx = find_first_op(data, start_idx=idx + 1)
                return node
            if data[idx] == "L":
                prev_idx = idx
                idx = find_first_op(data, start_idx=idx+1)
                node.left = TreeNode(int(data[prev_idx+1:idx]))
                node.left = dfs(node.left)
                return dfs(node)
            if data[idx] == "R":
                prev_idx = idx
                idx = find_first_op(data, start_idx=idx+1)
                node.right = TreeNode(int(data[prev_idx + 1:idx]))
                node.right = dfs(node.right)
                return dfs(node)
            return node
        root = dfs(root)
        return root


if __name__ == '__main__':
    coded_tree = Codec().deserialize("1R3L4L6UR7UUR5UUU")
    pass