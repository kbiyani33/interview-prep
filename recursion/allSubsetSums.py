from typing import List,Set
class Solution:
	def subsetSums(self, arr:List[int], n:int) -> List[int]:
		subsetSums = []
		for i in range(1<<n):
			subsetSum = 0
			for j in range(n):
				if i>>j & 1:
					subsetSum += arr[j]
			subsetSums.append(subsetSum)
		return subsetSums