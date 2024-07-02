class Solution:
	def nthPowerOfMid(self, mid, n, m): # return 0 if equal, 1 if less 2 if greater
		power = 1
		for i in range(n):
			power *= mid
			if power > m: return 2
		if power==m: return 0
		else: return 1
		
	def NthRoot(self, n:int, m:int) -> int:
		# Code here
		if m<=1:
			return m
		ans, low, high = -1, 1, m
		while low<=high:
			mid = low + (high-low)//2
			# nThPoWerOfMid = mid**n # THIS IS NOT GOOD EVER :)
			
			nThPowerInRange = self.nthPowerOfMid(mid, n, m)
			if nThPowerInRange == 0:
				return mid
			if nThPowerInRange == 1:
				low = mid+1
			else:
				high = mid-1
		return ans
		   
		 