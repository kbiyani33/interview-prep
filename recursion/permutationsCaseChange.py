"""
For input "ab" we need to genrate the following data
ab
aB
Ab
AB
"""
from typing import List

def getPermutationsHelper(input:any, permutations:List[any], op):
    if len(input) == 0:
        permutations.append(op)
        return
    
    op1 = op
    op2 = op

    # in op1 we will not make input[0] upper case
    # in op2 we will make input[0] upper case
    
    op1 += input[0]
    op2 += str(input[0]).upper()
    getPermutationsHelper(input[1:], permutations, op1)
    getPermutationsHelper(input[1:], permutations, op2)
    # changing op1 and op2 will basically reverse the output array
    

def permutationsWithCaseChange(input:any, permutations:List[any]):
    op = ""
    getPermutationsHelper(input, permutations, op)

if __name__ == "__main__":
    input = "ab"
    permutations = []
    permutationsWithCaseChange(input, permutations)
    print(permutations)