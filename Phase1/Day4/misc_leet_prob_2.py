'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
from builtins import *
class Solution:
    'this string can be used for documenting the information about class'
    def addNumFromList(listA, listB):
        temp_listA = listA[::-1]
        temp_listB= listB[::-1] 
            
        temp_list = []
        strA = ''
        strB = ''
        for keyA in temp_listA:
            strA = strA+str(keyA)
     
        for keyB in temp_listB:
            strB = strB+str(keyB)
         
        tempNumA = int(strA)
        tempNumB = int(strB)
        tempSum = tempNumA + tempNumB
         
        for index in str(tempSum):
            temp_list.append(int(index))
         
        return temp_list



    listA = [2,4,3]
    listB = [5,6,4]
    
    print(addNumFromList(listA, listB))