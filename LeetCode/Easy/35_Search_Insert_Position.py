"""
35. SEARCH INDEX POSITION
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""
first solution:
(26ms/89.94%)(13.84MB/95.76%)
using pointers
1. start with front and back pointers
2. change pointers by the halves until either
target is found or there are no numbers left
"""
def searchInsert(nums, target):
    f = 0
    b = len(nums)-1
    while f <= b:
        m = (b+f) // 2
        if nums[m] == target:
            return m
        #target is in front of m
        if nums[m] < target:
            f = m + 1
        else:
            b = m - 1
    return f

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums,target))
    target2 = 2
    print(searchInsert(nums,target2))
