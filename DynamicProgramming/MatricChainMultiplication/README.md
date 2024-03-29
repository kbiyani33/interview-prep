## MCM

### Problem Variations

1. Matrix Chain Multiplication
2. Printing MCM
3. Evaluate Expression to True/Boolean Parenthesis
4. Minimum Maximum Value of an expression
5. Palindromic Partitionining
6. Scramble String
7. Egg Drop

In matrix chain multiplication, problem, we have the following base format:

initialize i and j and k

```PYTHON
def solve(i, j, k, ip:any):
    # base condition
    # base condition is simple, if i > j
    temp1 = solve(i, k+1, k, ip)
    temp2 = solve(k+1, j, k, ip)

    #Run a function on temp1 and temp2 and get final response
```

### BASICS

For 2 matrices of size a*b and c*d respectively, then :
1. they can be multiplied if and only if b = c
2. Output is of size a*d
3. Cost of the multiplication of matrix = a*(b or c since equal)*d


E.g.
Suppose A, B C are 3 matrices of sizes 10*30, 30*5 and 5*60 respentively. Then:
- OP Dimension of (AB)C = 10*60 and cost = 10*30*5 + 10*5*60 = 4500
- OP Dimension of A(BC) = 10*60 and cost = 30*5*60 + 10*30*60 = 2700

Now minimum is 2700 so that becomes the possible cost.
