# # li1 = [1,2,3,4,5,6,7,8]
# # li2 = [8,7,6,5,4,3,2,1]
# #
# # print(li1)
# #
# #
# # print('slice from start till index n', li1[:5])
# #
# # print(li1[1:5])
# #
# # #Starts with 1
# # print(li1[1:])
# #
# # #Starts with 4
# # print(li1[4:])
# #
# # #to skip the step at regular pattern
# #
# # # start : end : number of elements to skip ==> STEPS
# # print(li1[0:6:2])
# #
# # # start with 0 index , go to lat index and skip 3 elemetns at a time
# # print(li1[0::3])
# #
# # #reverse : start from 0 index, go to last index and skip 1 elemets at a time
# # print(li1[::-1])
# #
# # print(li1[-6::2])
# #
# # #in the below line of code , it starts at index 7, goes to the end of index ,
# # # but the steps tp skip is 1, so it doensot find any number , will return empty list
# #
# # print(li1[7:0:1])
# #
# # #in the below code, it starts at 7 , goes to 0, and the steps to skip are the negetive manner , so basically it comes to 0 index reersing the list
# # print(li1[7:0:-1])

# #
# # print(li1==li2)
# #
# # print('minimum in list',min(li1))
# # print('maximum in list',max(li1))
# # print('length of list',len(li1))
# # print(li1*2)
#
# #list inside list
# listC = [1,2,['aa','bb'],3.112,['b',[11,22,33,['a','b']]],'r',[1,2,['x','y','z']]]
#
# print('length of list ',len(listC))
# print('value at index 2 -->',listC[2],'length of value at index 2 -->', len(listC[2]))
# print('value at index 0 of index 2 of list ->',listC[2][0],'\n'
#       'value at index 1 of index 2 of list ->',listC[2][1])
# print(listC[-2])
#
# print(listC[4][1][3])

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1,1):
        if i%3==0 and i%5 ==0:
            print(i)
            print('FizzBuzz')
        if i%3==0 and not(i%5 == 0):
            print('Fizz')
        if i%5 ==0 and i%3 != 0:
            print('Buzz')
        if i%3 != 0 and i%5 != 0:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
