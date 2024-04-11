from typing import List
import math

class MyMinHeap:
    """
    Min heap is a complete binary tree. In which:
        a. All levels are filled without gaps from left to right.
        b. The parent is always smaller than it's children recursively from root to the leaves of the tree.
    
    Its easily represented as an array. Root is arr[0]

    left child for index i      = arr[(2*index)+1]
    right child for index i     = arr[(2*index)+2]
    parent of index i           = (i-1)//2
    """
    def __init__(self, heap:List[any] = []):
        self.arr = heap
        i = (len(heap) - 2) // 2   # finding the right most internal node and reducing it's values by one on each iteration.

        while i >= 0:
            self.minHeapify(i)
            i = i - 1
    
    def getParent(self, index:int) -> int:
        return (index-1)//2

    def getLeftChild(self, index:int) -> int:
        return (2*index) + 1
    
    def getRightChild(self, index:int) -> int:
        return (2*index) + 2
    
    def insertElement(self, element:int):
        """
        insert at end of the list and compare with it's parent. If it's smaller than parent then swap.
        Do this until we -
            1. Either reach root of the array
            2. Find a position where element is larger than it's parent.
        """

        arr = self.arr
        arr.append(element)
        elementPosition = len(arr) -1
        while(elementPosition > 0 and element < arr[self.getParent(elementPosition)]):
            parentPosition = self.getParent(elementPosition)
            arr[elementPosition], arr[parentPosition] = arr[parentPosition], arr[elementPosition]
            elementPosition = parentPosition
        
        return
    
    def minHeapify(self, index:int=0):
        """
        minHeapify is a process that is done, when root is not following the heap properties and we have to make it correct.
        we start from root and find the minimum value in bw it's root, left and right children and swap them.
        Then recursively call it on the minimum side.
        We do this until we come to a place where we have the root at the maximum value.
        """
        
        arr = self.arr
        size = len(arr)

        smallest = index
        leftChild = self.getLeftChild(index)
        rightChild = self.getRightChild(index)

        if leftChild < size and arr[leftChild] < arr[index]:
            smallest = leftChild
        if rightChild < size and arr[rightChild] < arr[index]:
            smallest = rightChild
        
        if smallest == index:
            return
        
        arr[smallest], arr[index] = arr[index], arr[smallest]
        self.minHeapify(smallest)
    
    def extractMin(self) -> int:
        """
        This has 3 steps
            1. replace arr[0] with arr[len(arr)-1]
            2. pop last element
            3. minHeapify
        """
        arr = self.arr
        if len(arr) == 0:
            return -math.inf
        
        res = arr[0]
        arr[0] = arr[len(arr) - 1]
        arr.pop()

        self.minHeapify()
        return res
    
    def decreseKey(self, index:int, value:int):
        """
        this function replaces the value of an element at index with new value.
        """
        arr = self.arr
        if index >= len(arr):
            return
        arr[index] = value 
        while index > 0 and arr[index] < arr[self.getParent(index=index)]:
            parent = self.getParent(index)
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
    
    def deleteValue(self, index:int):
        """
        this deletes the element at index and makes sure heap properties are maintained.
        """
        arr = self.arr
        if index >= len(arr):
            return
        
        self.decreseKey(index, -math.inf)
        return self.extractMin()

        
        


        

