class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def insertWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()

            curr = curr.children[w]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        rows, cols = len(board), len(board[0])
        trieObj = TrieNode()
        op = []
        visited = [[False for i in range(cols)] for j in range(rows)]
        res = set()

        # create a Trie with all the words
        for word in words:
            trieObj.insertWord(word)

        def oob(i, j):
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
                return True
            return False

        def travel(i, j, currNode, word):

            # if out of bounds, return
            if oob(i, j):
                return

            # if visiting, or cycle, return
            if visited[i][j]:
                return

            # if reached end of board, return
            if i == rows and j == cols:
                return

            # if the current letter is not child of Trie node, return
            if board[i][j] not in currNode.children:
                return

            # mark the visited
            visited[i][j] = True

            currNode = currNode.children[board[i][j]]
            word += board[i][j]
            if currNode.isWord:
                res.add(word)

            travel(i + 1, j, currNode, word)
            travel(i, j + 1, currNode, word)
            travel(i - 1, j, currNode, word)
            travel(i, j - 1, currNode, word)

            # mark the visited False
            visited[i][j] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                travel(i, j, trieObj, "")
