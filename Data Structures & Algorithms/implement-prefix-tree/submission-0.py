'''
step 1: define a TrieNode with a children dictionary and an isWord flag.
step 2: initialize a PrefixTree with a root Trienode.
step 3: for insert, traverse each character and create missing nodes.
step 4: for search, traverse each character and check isWord at the end.
step 5: for startsWith, traverse the prefix and return if the path exists.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return True
        
        