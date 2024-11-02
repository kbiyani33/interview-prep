from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:

    def __init__(self):
        self.chars = [None]*26
        self.wordEndsHere = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word:str):
        temp = self.roots
        for i in range(len(word)):
            charIndex = ord(word[i]) - 97
            if not temp.chars[charIndex]:
                temp.chars[charIndex] = TrieNode()
            temp = temp.chars[charIndex]
        temp.wordEndsHere = True
    
    def checkWordExists(self, word:str) -> bool:
        temp = self.root
        for i in range(len(word)):
            charIndex = ord(word[i]) - 97
            if not temp.chars[charIndex] or not temp.chars[charIndex].wordEndsHere: 
                return False
            temp = temp.chars[charIndex]
        return temp.wordEndsHere

def lexicographical(st1:str, st2:str):
    for i in range(len(st1)):
        if st1[i]==st2[i]:
            continue
        if ord(st1[i]) < ord(st2[i]): return st1
        else: return st2

def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    for word in a:
        trie.insertWord(word)
    # Now I'll find the largest word with all prefixes
    maxLen = 0
    res = ""
    for word in a:
        if trie.checkWordExists(word):
            if len(word) > maxLen:
                maxLen = len(word)
                res = word
            elif len(word) == maxLen:
                res = lexicographical(word, res)
    if maxLen > 0: return res
    return None