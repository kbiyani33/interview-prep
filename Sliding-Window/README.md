## Idea and Identification
A subarray or substring if a contiguous block of an array or a continous block of a string within the input string.

A sliding window is always continous.

The input is an array or string, and the question is about a subarray of a substring. 
The question is going to be find a largest/smallest of the substring/subarray.
And there is a window size K which is either given or it's being found.

## Types of Sliding Window

### Fixed Size Sliding Window
K(Window size is fixed). Here the question is to find the sum

### Variable Size Sliding Window
K(Window size is being asked.) The question is to find the largest window or the smallest window subject to a constraint. 
In this case one example is that the sum required is say T. So one possible question is to find the maximum window with sum T.

E.g. [3,2,4,5,1,1,1,1,1,3,5]
Suppose the sum is needed as 5. The following are possible subarrays that have sum as 5
3,2
5
1,1,1,1,1
1,1,3
In all the above cases, maximum size of the sliding window is 5 so that's the output. 


### Problems on Sliding Window to be discussed
We have around 10 questions. 5 Fixed Size and 5 Variable size window.

#### Fixed Size Window Problems
1. Max/Min aum subarray of size K
2. 1st negative in every window of size K
3. Count occurences of anagram
4. Maximum of all subarrays of size k
5. Maximum and Minimum for every window size

#### Variable Size Window Problems
1. Largest/Smallest subarray of size K
2. Largest substring of K distinct characters
3. Length of largest substring with no repeating characters
4. Pick Toy
5. Minimum Window Substring(v.v.v. important)