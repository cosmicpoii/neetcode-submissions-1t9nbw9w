'''
step 1: build a Trie from all words
step 2: run DFS from every cell on the board
step 3: if the current board character is not in the current TrieNode's children,
        we stop early because no word can start with this path
step 4: when we reach a TrieNode that stores a word, we add it to the result
        and set it to None to avoid duplicates
step 5: use backtracking to mark visisted cells and restore them after exploring
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"

            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)


        return res