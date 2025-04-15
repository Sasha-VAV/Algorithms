class WordDictionary:
    class Node:
        def __init__(self, val, is_end=0, nodes=None):
            self.val = val
            self.is_end = is_end
            self.nodes = list() if nodes is None else nodes
    def __init__(self):
        self.nodes = []

    def addWord(self, word: str, nodes=None) -> None:
        nodes = self.nodes if nodes is None else nodes
        for node in nodes:
            if node.val == word[0]:
                if len(word) == 1:
                    node.is_end = 1
                    return
                self.addWord(word[1:], node.nodes)
                return
        new_node = self.Node(word[0])
        if len(word) == 1:
            new_node.is_end = 1
        else:
            self.addWord(word[1:], new_node.nodes)
        nodes.append(new_node)

    def search(self, word: str, nodes=None) -> bool:
        nodes = self.nodes if nodes is None else nodes
        for node in nodes:
            if node.val == word[0] or word[0] == ".":
                if len(word) == 1 and node.is_end == 1:
                    return True
                elif len(word) == 1 and node.is_end == 0 and word[0] != ".":
                    return False
                elif self.search(word[1:], node.nodes):
                    return True
                elif word[0] != ".":
                    return False
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)