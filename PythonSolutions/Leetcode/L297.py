from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        nodes = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node is None:
                nodes.append("N")
            else:
                nodes.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        nodes.pop(0)
        q = deque()
        q.appendleft(root)
        while q:
            node = q.popleft()
            left = nodes.pop(0)
            right = nodes.pop(0)
            if left == "N":
                node.left = None
            else:
                node.left = TreeNode(int(left))
                q.append(node.left)
            if right == "N":
                node.right = None
            else:
                node.right = TreeNode(int(right))
                q.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
if __name__ == '__main__':
    tree = Codec().deserialize("1,2,3,N,4,N,N,N,N")
    tree = Codec().serialize(tree)
    print(tree)
    tree = Codec().deserialize(tree)
    pass
