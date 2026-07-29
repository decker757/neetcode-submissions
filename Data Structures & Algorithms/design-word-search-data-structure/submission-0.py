class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isLast = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            for j in range(i, len(word)):
                ch = word[j]
                if ch == ".":
                    for child in node.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.isLast

        
        return dfs(0, self.root)
                
