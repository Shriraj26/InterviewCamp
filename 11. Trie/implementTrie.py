"""
Watch the neetcode video for more details!! - 
https://www.youtube.com/watch?v=oobqoCJlHA0
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str) -> None:
        curr = self.root
        for c in s:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        if not curr.isWord:
            return False
        return True

    def startsWith(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True

    def searchWithDots(self, word):

        def dfs(j, root):

            curr = root

            for i in range(j, len(word)):
                currLetter = word[i]

                if currLetter == '.':

                    # check for all the children of the current node
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if currLetter not in curr.children:
                        return False
                    curr = curr.children[currLetter]

            return curr.isWord

        dfs(0, self.root)



