from os import *
from sys import *
from collections import *
from math import *

class TrieNode:

    def __init__(self):
        self.chars = [None]*26
        self.endsWith = 0
        self.prefixWith = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            charsIndex = ord(ch)-97
            if not temp.chars[charsIndex]:
                temp.chars[charsIndex] = TrieNode()
            temp.chars[charsIndex].prefixWith += 1
            temp = temp.chars[charsIndex]
        temp.endsWith += 1

    def countWordsEqualTo(self, word):
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            charsIndex = ord(ch) - 97
            if not temp.chars[charsIndex]:
                return 0
            temp = temp.chars[charsIndex]
        return temp.endsWith

    def countWordsStartingWith(self, word):
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            charsIndex = ord(ch) - 97
            if not temp.chars[charsIndex]:
                return 0
            temp = temp.chars[charsIndex]
        return temp.prefixWith

    def erase(self, word):
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            charsIndex = ord(ch) - 97
            temp.chars[charsIndex].prefixWith -= 1
            temp = temp.chars[charsIndex]
        if temp.endsWith > 1: temp.endsWith -= 1
        # return temp.endsWith
