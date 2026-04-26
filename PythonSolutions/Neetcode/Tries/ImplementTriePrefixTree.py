class PrefixTree:
    class Node:
        def __init__(self, val, nodes=None, is_suffix=False):
            self.val = val
            self.nodes = nodes
            self.is_suffix = is_suffix
    def __init__(self):
        self.nodes = None
    def search_prefix(self, word, node=None):
        if node is None:
            nodes = self.nodes
        else:
            nodes = node.nodes
        for x in nodes:
            if word.startswith(x.val) == 0:
                return self.search_prefix(word, x)
        return node

    def insert(self, word: str) -> None:
        node = self.search_prefix(word)
        if node is None:
            self.nodes.append(PrefixTree.Node(word))
            return
        if node.val == word:
            node.is_suffix = False
            return


    def search(self, word: str) -> bool:
        ...

    def startsWith(self, prefix: str) -> bool:
        ...

