class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = float('inf')
        self.best_len = float('inf')

class Solution:
    def stringIndices(self, words_container: List[str], words_query: List[str]) -> List[int]:
        root = TrieNode()
        for i, word in enumerate(words_container):
            n = len(word)
            curr = root

            if n < curr.best_len:
                curr.best_len = n
                curr.best_idx = i
            
            for c in reversed(word):
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c]

                if n < curr.best_len:
                    curr.best_len = n
                    curr.best_idx = i
            
        res = []

        for query in words_query:
            curr = root
            for c in reversed(query):
                if c not in curr.children:
                    break
                curr = curr.children[c]
            res.append(curr.best_idx)
        return res