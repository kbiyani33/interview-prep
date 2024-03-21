"""
Same as permutations case change. However, a character can be both digit and in upper case from before.

if IP = a1B2
OP = 
a1b2
a1B2
A1b2
A1B2
"""
from typing import List

def getPermutationsHelper(input:any, permutations:List[any], op):
    if len(input) == 0:
        permutations.append(op)
        return
    
    if str(input[0]).isdigit():
        # in this case we simply add input[0] to the op and call the function again
        op += input[0]
        getPermutationsHelper(input[1:], permutations, op)
    else:
        op1 = op
        op2 = op

        # in op1 we will take input[0] in lower case
        # in op1 we will take input[0] in upper case
        
        op1 += str(input[0]).lower()
        op2 += str(input[0]).upper()
        getPermutationsHelper(input[1:], permutations, op1)
        getPermutationsHelper(input[1:], permutations, op2)
    

def permutationsWithCaseChange(input:any, permutations:List[any]):
    op = ""
    getPermutationsHelper(input, permutations, op)

if __name__ == "__main__":
    input = "a1B2"
    permutations = []
    permutationsWithCaseChange(input, permutations)
    print(permutations)