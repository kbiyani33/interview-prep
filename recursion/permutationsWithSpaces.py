"""
For a string abc
print
a b c
a bc
ab c
abc


Basically we have to insert spaces in between the characters.
And get all posssible values.

CHOICE DIAGRAM

Now note that we don't have to worry about the space for the ending characters.

Let IP = "ABC" and OP = ""

When taking first character, I have to include A as it is. No concept of space before A exists.

So IP = "BC" and OP = "A"

Now I have include B with spaces or without space
With space      --> IP = "C" and OP = "A B"
Without space   --> IP = "C" and OP = "AB"

Now I have C, which can be included with or without spaces
With space      --> IP = "" and OP = "A B "
Without space   --> IP = "" and OP = "AB C"
"""

from typing import List

def getPermutationsHelper(input:any, permutations:List[any], op):
    if len(input) == 0:
        permutations.append(op)
        return
    
    op1 = op
    op2 = op

    # in op1 we won't include space to input[0]
    # in op2 we will include space
    op1 += " " + input[0]
    op2 += input[0]
    # in op1 i will not include input 0 and the input will not contain it
    # in op2 i will include input 0 and input will again not contain it
    getPermutationsHelper(input[1:], permutations, op1)
    getPermutationsHelper(input[1:], permutations, op2)
    # changing op1 and op2 will basically reverse the output array
    

def permutationsWithSpaces(input:any, permutations:List[any]):
    if len(input) == 0:
        return
    op = input[0]
    getPermutationsHelper(input[1:], permutations, op)

if __name__ == "__main__":
    input = "abc"
    permutations = []
    permutationsWithSpaces(input, permutations)
    print(permutations)