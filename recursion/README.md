## RECURSION

We will have one of the two ways to solve a recursive problem.

### INDUCTION BASE HYPOTHESIS

Very useful for tree based and LL based problems for O(1)

In this we divide the problem into 3 parts :
1. Hypothesis
2. Induction
3. Base Condition

Suppose we take the problem of Height of Binary tree problem

1. ##### Hypothesis
Suppose the function is HeightOfBinary(root:Node) --> This will return the height of the bianry tree the root of which is in the input.
Hypothesis is a simple statement. That's all.

2. ##### Induction
In induction we use the Principle of mathematical induction. If i am able to get the height of root of binary tree, i can get the height of left and right subtrees as well
So I can get HeightOfBinary(root.left) and HeightOfBinary(root.right)

And if I get left and right heights, my original tree's height is max(lh, rh) + 1

3. ##### Base Condition
We get the smallest possible input.