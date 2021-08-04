'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


def twoSum(nums, target):
    remaining_item_dict = {}
    for key, value in enumerate(nums):
        remained_int = target-value
        if remained_int in remaining_item_dict:
            return [remaining_item_dict[remained_int], key]
        remaining_item_dict[value] = key
    
    return []

nums = [3,4,7,6]
target = 9

res = twoSum(nums,target)

print(res)