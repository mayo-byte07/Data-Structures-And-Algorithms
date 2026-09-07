class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
        return dfs(0, self.root)