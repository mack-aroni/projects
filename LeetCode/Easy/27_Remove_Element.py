"""
27. REMOVE ELEMENT
Given an integer array nums and an integer val, remove
all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements
in nums which are not equal to val.

Consider the number of elements in nums which are not equal
to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums
contain the elements which are not equal to val. The remaining
elements of nums are not important as well as the size of nums.

Return k.
"""

"""
first solution:
(18ms/59.77%)(13.2MB/88.54%)
change list
1. using static i, iterate over nums
2. if nums[i] == val, pop it off the list
3. else increase i and count
"""
def removeElement(nums, val):
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i = i + 1
            count = count + 1
    return count

"""
second solution:
(20ms/44.37%)(13.26MB/56.53%)
replace in place
1. static j holds index
2. iterate over nums
3. if nums[i] != val move it to nums[index]
4. return j which is count of non val
"""
def removeElement_2(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

"""
solution(not in place):
(11ms/96.17%)(13.36MB/24.08%)
use python to reformat the list
"""
def removeElement_3(nums, val):
    nums[:] = [num for num in nums if num != val]
    return len(nums)

if __name__ == "__main__":
    nums = [2,3,5]
    val = 3
    print(removeElement(nums,val))