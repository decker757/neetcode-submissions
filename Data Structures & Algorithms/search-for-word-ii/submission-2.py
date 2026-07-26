class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        root = TrieNode()
        res = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for w in words:
            root.addWord(w)

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= R or c >= C or board[r][c] == '#' or board[r][c] not in node.children):
                return
            
            temp = board[r][c]
            node = node.children[temp]
            word += temp
            board[r][c] = '#'
            if node.isWord:
                res.add(word)

            for dr, dc in directions:
                dfs(dr + r, dc + c, node, word)

            board[r][c] = temp

        for r in range(R):
            for c in range(C):
                dfs(r, c, root, "")
        
        return list(res)