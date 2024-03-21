from typing import List

"""
Variations

substring   --> for string abc... any contiguous block is a substring
subarray    --> any contiguous block within an array is a subarray

Subsequesce --> It need not be continuous block but it's order must be maintained
Subset      --> Order is also not needed.

Subset is superset of subsequence is superset of substring/substring

So the following code is same for

print powerset/subsets/subsequences etc

We may have to sort the array in ascending order(lexicographoically)
"""

def getSubsetsHelper(input:any, powerSet:List[any], op):
    if len(input) == 0:
        if op not in powerSet:
            powerSet.append(op)
        return
    
    op1 = op
    op2 = op

    firstElement = input[0]
    op2 += firstElement
    # in op1 i will not include input 0 and the input will not contain it
    # in op2 i will include input 0 and input will again not contain it
    getSubsetsHelper(input[1:], powerSet, op1)
    getSubsetsHelper(input[1:], powerSet, op2)
    

def getAllSubsets(input:any, powerSet:List[any]):
    op = ""
    getSubsetsHelper(input, powerSet, op)

if __name__ == "__main__":
    input = "aaaaa"
    powerSet = []
    getAllSubsets(input, powerSet)
    print(powerSet)