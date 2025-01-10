class Solution:
	def minCoins(self, coins, sum):
		if sum == 0:
			return 0
		coins.sort(reverse=True)
		remaining = sum
		index = 0
		count = 0
		picked = []
		while index < len(coins):
			if coins[index] > remaining:
				index += 1
				continue
			remaining -= coins[index]
			picked.append(coins[index])
			count += 1
			if remaining == 0:
				return (count, picked)
		return (-1, [])
	
if __name__=="__main__":
	soln = Solution()
	print(soln.minCoins(coins=[936,917,205,483,345,307,117,20,679], sum=6620))