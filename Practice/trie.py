class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr.children[letter] = TrieNode()

            curr = curr.children[letter]

        curr.isWord = True

    def search(self, word):

        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        if curr.isWord:
            return True
        return False

    def startsWith(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return True
