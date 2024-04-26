from typing import List
from collections import deque

class Solution:
	def wordLadderLength(self, startWord:str, targetWord:str, wordList:List[str]) -> int:
		if startWord==targetWord:
			return 1
		q = deque()
		q.append((startWord, 1)) # since we are starting from level 1
		wordSet = set(wordList)
		if startWord in wordSet:
			wordSet.remove(startWord)
		while len(q) > 0:
			word, level = q.popleft()
			for i in range(len(word)):
				for j in range(26):
					newChar = chr(j+97) # 97 because we want to only deal with small letter words. If not we convert everything to small letter words at the beginning and it then remains the same
					transformedWord = word[:i] + newChar + word[(i+1):]
					if transformedWord==targetWord:
						return level + 1
					if transformedWord in wordSet:
						wordSet.remove(transformedWord)# first of all remove this from the set
						q.append(transformedWord, level+1)
		return 0
        # it has come here it means it never gor the target word.
		# so as per question return 0
        
					