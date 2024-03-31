### Identification

There will be an array. 
Suppose you have written an O(N**2) solution in brute force.
Where outer loop is from 0 to N and inner loop is having one of the following 4 forms:

1. ```PYTHON
    for i in range(N):
        for j in range(i) # j++
    ```

2. ```PYTHON
    for i in range(N):
        for j in range(i, -1, -1) # j--
    ```

3. ```PYTHON
    for i in range(N):
        for j in range(i, N, 1) # j++
    ```

4. ```PYTHON
    for i in range(N):
        for j in range(N-1, i-1, -1) # j--
    ```

Then there is a 100% chance that a better solution can be written using stack. Note that this won't be necessary when the inner loop also is from 0 to N