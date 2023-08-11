"""
1. TWO SUM
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up
to target.

You may assume that each input would have exactly one
solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
first solution
brute force
1. iterate over nums
2. iterate forward over i, len(nums)
3. if nums[i] + nums[j] == target, return i, j
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1,l):
            if target == (nums[i] + nums[j]):
                return i, j
            
"""
better solution
hashing
1. iterate over nums
2. compare target - nums[i]
3. if n is in dict, return the indexes
4. else, add nums[i] to dict
"""
def twoSum_2(nums, target):
    dict = {}
    for i in range(len(nums)):
        n = target - nums[i]
        if n in dict:
            return i, dict[n]
        dict[nums[i]] = i
    

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    nums_2 = [3,2,4]
    target_2 = 6
    nums_3 = [3,3]
    target_3 = 6
    print(twoSum_2(nums,target))