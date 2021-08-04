from collections import *

listA = [2, 3, 4, 2, 3, ]

listB = [x for x in listA]

listC = ['amit', 'Sumit']

listD = listC.extend(listB[:len(listB)])

#listD = listC

''' if we place listC in place of listD here , it is returning  None Value , why ? '''

print('list A = ', listA)

print('list B = ', listB)

print('list C = ', listC)

''' why is this list collecting garbage value ? '''

print('list D = ', listD)

''' '''

