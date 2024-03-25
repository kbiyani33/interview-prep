"""
Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert the minimum number of characters from/in str1 to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted at some another point.

Example 1: 

Input : 
str1 = "heap", str2 = "pea" 
Output : 
Minimum Deletion = 2 and
Minimum Insertion = 1
Explanation:
p and h deleted from heap
Then, p is inserted at the beginning
One thing to note, though p was required yet
it was removed/deleted first from its position and
then it is inserted to some other position.
Thus, p contributes one to the deletion_count
and one to the insertion_count.




Algorithm: 

str1 and str2 be the given strings.
m and n be their lengths respectively.
len be the length of the longest common subsequence of str1 and str2
minimum number of deletions minDel = m – len (as we only need to delete from str1 because we are reducing it to str2)
minimum number of Insertions minInsert = n – len (as we are inserting x in str1 , x is a number of characters in str2 which are not taking part in the string which is longest common subsequence )
"""


