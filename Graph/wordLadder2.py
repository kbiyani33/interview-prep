#User function Template for python3
from typing import List, Union
from collections import deque

class Solution:
    def findSequences(self, startWord: str, targetWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []  # list to hold the answer
        vis = set(wordList)  # set to keep track of visited words
        usedOnLvl = []  # list to hold the words used on the current level
        q = deque()  # deque to implement the BFS
        q.append([startWord])  # start the BFS with the initial word
        level = 0  # current level
         
        # Implement BFS
        while q:
            vec = q.popleft()  # get the first word in the deque
            if len(vec) > level:
                level += 1
                for str in usedOnLvl:
                    if str in vis:
                        vis.remove(str)  # remove the words used on the current level from the visited set
                usedOnLvl = []  # reset the list of words used on the current level
             
            last = vec[-1]  # get the last word in the sequence
            if last == targetWord:
                if not ans:
                    ans.append(vec)  # if the answer is empty, add the sequence
                elif len(ans[0]) == len(vec):
                    ans.append(vec)  # if the length of the sequence is equal to the first sequence in the answer, add the sequence
             
            for i in range(len(last)):
                org = last[i]  # store the original character
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    last = last[:i] + c + last[i+1:]  # replace the current character with a new character
                    if last in vis:
                        vec.append(last)  # add the new word to the sequence
                        q.append(vec.copy())  # add the new sequence to the deque
                        vec.pop()  # remove the new word from the sequence
                        usedOnLvl.append(last)  # add the new word to the list of words used on the current level
                last = last[:i] + org + last[i+1:]  # restore the original character
         
        return ans  # return the answer