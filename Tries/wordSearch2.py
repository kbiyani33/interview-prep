from typing import List,Optional

class TrieNode:
    def __init__(self):
        self.chars = [None]*26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertWord(self, word:str):
        temp = self.root
        for i in range(len(word)):
            charIndex = ord(word[i]) - 97
            if not temp.chars[charIndex]:
                temp.chars[charIndex] = TrieNode()
            temp = temp.chars[charIndex]
        temp.endOfWord = True


class Solution:
    def dfs(self, board: List[List[str]], trie:Trie, row:int, col:int, path:List[str], ans:set, visited:set):
        # if I have already reached the end of the word, then wonderful.
        if trie.endOfWord:
            ans.add("".join(path))
            trie.endOfWord = False # to avoid duplicate additions to answer
            # here we are not going to return since it's possible to have a case like ab one word and abc another word.
            # If i return, i'll miss words that don't end here, but are having this as a prefix
        
        m, n = len(board), len(board[0])
        if (row<0 or row>=m or
            col<0 or col>=n or
            (row,col) in visited):
            return
        
        char = board[row][col]
        if not trie or not trie.chars[ord(char) - ord("a")]:
            return
        
        path.append(char)
        visited.add((row, col))
        trieNext = trie.chars[ord(char) - ord("a")]
        # we can move in 4 directions
        self.dfs(board, trieNext, row, col-1, path, ans, visited)
        self.dfs(board, trieNext, row-1, col, path, ans, visited)
        self.dfs(board, trieNext, row, col+1, path, ans, visited)
        self.dfs(board, trieNext, row+1, col, path, ans, visited)

        # backtracking
        path.pop()
        visited.remove((row, col))
        return

    def searchWords(self, board: List[List[str]], trie:Trie) -> List[str]:
        m, n = len(board), len(board[0])
        ans = set()
        for i in range(m):
            for j in range(n):
                # the idea is that, I will check if there is a word starting with the current char
                trieCharIndex = ord(board[i][j]) - ord("a")
                if not trie.root.chars[trieCharIndex]:
                    continue
                # now I will start a dfs path with this trie
                self.dfs(board, trie.root, i, j, [], ans, set())
        return list(ans)
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return [] # edge case of an empty board
        trie = Trie()
        for word in words:
            trie.insertWord(word)
        return self.searchWords(board, trie)
        