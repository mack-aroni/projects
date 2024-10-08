"""
26. REMOVE DUPLICATES FROM SORTED ARRAY
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

"""
first solution:
(115ms/20.20%)(14.4MB/73.79%)
brute force
1. iterate over nums, from 0 to len-1
2. if duplicate, pop from nums and resume at i
3. else increase count and i
"""


def removeDuplicates(nums):
    count = 1
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            count = count + 1
            i = i + 1
    return count


"""
second solution:
(57ms/84.77%)(14.8MB/26.8%)
replace in place
1. static j holds index
2. iterate over nums from 1 to len
3. if duplicate replace nums[i] with
the duplicate
4. return j which is unique count
"""


def removeDuplicates_2(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3]
    print(removeDuplicates(nums))
