class Solution:
	def recursive(self, arr, n, index, sum, dp):
		MOD = 1000000007
		if index >= n:
			if sum == 0: return 1
			else: return 0
			
		if dp[index][sum] != -1: return dp[index][sum]
		notPick = self.recursive(arr, n, index+1, sum, dp)
		if arr[index]>sum:
			dp[index][sum] = notPick
		else:
			pick = self.recursive(arr, n, index+1, sum-arr[index], dp)
			dp[index][sum] = (pick%MOD+notPick%MOD)%MOD
		
		return dp[index][sum]
		
	def perfectSum(self, arr, n, sum):
		# code here
		dp = [[-1 for _ in range(sum+1)] for _ in range(n)]
		return self.recursive(arr, n, 0, sum, dp)
	
	def tabulationDP(self, arr, n, sum):
		dp = [[0 for _ in range(sum+1)] for _ in range(n+1)]
		MOD = 1000000007
		for i in range(n+1):
			dp[i][0] = 1
		for i in range(n-1, -1, -1):
			for j in range(1, sum+1):
				if arr[i] > j:
					dp[i][j] = dp[i+1][j]
				else:
					dp[i][j] = (dp[i+1][j] %MOD +dp[i+1][j-arr[i]] % MOD) % MOD
		return dp[0][sum]
	
        