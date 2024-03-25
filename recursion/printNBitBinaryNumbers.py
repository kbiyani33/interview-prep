"""
For an input N, print the total number of n bit binary numbers for which,
the number of 1's in all the prefixes is greater than or equal to number of 0's

Example 1:

Input:  
n = 2
Output: 
"11, 10"
Explanation: Valid numbers are those where each prefix has more 1s than 0s:
11: all its prefixes (1 and 11) have more 1s than 0s.
10: all its prefixes (1 and 10) have more 1s than 0s.
So, the output is "11, 10".
Example 2:

Input:  
n = 3
Output: 
"111, 110, 101"
Explanation: Valid numbers are those where each prefix has more 1s than 0s.
111: all its prefixes (1, 11, and 111) have more 1s than 0s.
110: all its prefixes (1, 11, and 110) have more 1s than 0s.
101: all its prefixes (1, 10, and 101) have more 1s than 0s.
So, the output is "111, 110, 101".
"""
from typing import List

def getAllNBitBinaryNumbers(allNBitBinaryNumbers:List[str], n0:int, n1:int, op:str, N:int):
    if n0 + n1 == N:
        allNBitBinaryNumbers.append(op)
        return
    
    op1 = op + "1"
    getAllNBitBinaryNumbers(allNBitBinaryNumbers, n0, n1+1, op1, N)
    
    if n1 > n0:
        op2 = op + "0"
        getAllNBitBinaryNumbers(allNBitBinaryNumbers, n0+1, n1, op2, N)

if __name__ == "__main__":
    n = int(input("Number of bits needed ins string ? "))
    allNBitBinaryNumbers = []
    n0 = 0
    n1 = 0
    op = ""
    getAllNBitBinaryNumbers(allNBitBinaryNumbers, n0, n1, op, n)
    print(allNBitBinaryNumbers)