from array import *

arrayName = array('i', [10, 20, 30, 40, 50])

arrayName.insert(1, 11)

print("Complete Array :  ", arrayName)

for i  in arrayName:
    print(f"{i+1}th index of Array {arrayName[i]} ")
