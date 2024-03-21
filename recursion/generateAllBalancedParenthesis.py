from collections import deque
from typing import List

def generateAllParenthesis(allParenthesis:List[str], opening:int, closing:int, op:str):
    if opening == 0 and closing == 0:
        allParenthesis.append(op)
        return
    
    if opening != 0:
        op1 = op + "("
        generateAllParenthesis(allParenthesis, opening-1, closing, op1)
    
    if closing >opening:
        op1 = op + ")"
        generateAllParenthesis(allParenthesis, opening, closing-1, op1)


if __name__ == "__main__":
    n = int(input("how many opening and closing parenthesis are needed ? "))
    allParenthesis = []
    opening = n
    closing = n
    op = ""
    generateAllParenthesis(allParenthesis, opening, closing, op)
    print(allParenthesis)