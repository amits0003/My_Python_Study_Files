'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

def checkTwoSum(num,target):
    new_dict = {}
    for key, value in enumerate(num):
        temp_int = target - value
        if (temp_int in new_dict):
            return [new_dict[temp_int], key]
        new_dict[value] = key
        
    return ("Combination not possible")
    
numList = [2,3,4,5]

target = 8

res = checkTwoSum(numList, target)

print(res)
            