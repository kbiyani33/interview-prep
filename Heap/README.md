## Identification

If we are given an array and have been asked minimum/maximum of some condition with a given K then we can use heap.

Heap is of 2 types
- Min Heap (For Maximum/Largest of some condition) --> In this minimum element is on the top.
- Max Heap (For Minimum/Smallest of some condition) --> In this maximum element is on the top.

In most questions, we can simply use the idea of sorting with K in question. So complexity becomes nlogK.

### Example
Kth Smallest Element in an array. Regular way is to sort the array and get the 3rd smallest accordingly. However it is NlogN Time Complexity.

Since it's only asked for Kth, can we reduce the work done on the N-K Elements ?

We will use max heap for until we have k elements. 

1. Traverse the array
    a. If empty heap, simply enter
    b. If val>top of heap - simply push element to top of heap
    c. If smaller - Push element to bottom of heap
    d. If size of heap>K:
        pop the top
        ## Will remove the element from 10

2. return top of heap

Hence if we are looking Kth smallest, we will need max heap to remove the larger elements and vice versa.

MAX Heap is priority queue
MIN Heap is priority qyeue with pair<int, int>, greater

