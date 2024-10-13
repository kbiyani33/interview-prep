from typing import List

class Solution:
    # O(2N) T and O(2N) S
    def bruteForce(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [1]*n, [1]*n

        # first left
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        
        # next right
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        
        # get the maximum and the sum
        candies = 0
        for i in range(n):
            candies += max(left[i], right[i])
        return candies
    
    # O(2N) T and O(N) space
    def better(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [1]*n, [1]*n

        # first left
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        
        # next right
        current = 1 # since last last will start with right
        right =  1 # since i need to keep track of this
        candies = max(1, left[n-1]) # to get the count of candies to be returned
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                current = right + 1
            else:
                current = 1
            if i==n-2:
                secondLast = max(left[i], current)
            candies += max(left[i], current)
            right = current
        # we have missed the last element in loop which we covered in the initialisation
        # since if the last value is same as previous value, it'll get 1 which we can get using left
        return candies
            