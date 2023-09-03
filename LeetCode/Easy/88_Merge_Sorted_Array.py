"""
88. MERGE SORTED ARRAY
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the last
n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

"""
first solution:
(18ms/76.05%)(13.20MB/59.09%)
list manipulation
1. create index variable
2. iterate until nums2 is empty or nums2 > nums1[i]
3. while in loop, if first index of nums2 < nums1[i]
insert it at index i and pop the end (removes 0) and
increment i
4. at the end if nums2 is not empty, add it to the 
remaining slots in nums1
"""
def merge(nums1, m, nums2, n):
    i = 0
    #i < m+(n-len(nums2)) is if an index of nums2 isnt
    #added to nums1, so i exceed that value
    while nums2 and i < m+(n-len(nums2)):
        print(nums1,nums2,i)
        if nums2[0] < nums1[i]:
            nums1.insert(i,nums2.pop(0))
            nums1.pop()
        i = i + 1
    if nums2:
        for x in nums2:
            nums1[i] = x
            i = i + 1
    return nums1

"""
second solution:
(15ms/88.05%)(13.40MB/25.62%)
reverse pointers
1. create two rear pointers for nums1 and
nums2 and a back pointer for nums1
2. if nums1[i] > nums[j] and i >= 0,
set nums1[k] to nums1[i] and decrement i
(nums1[i] is larger than nums2[i] and should
be at the end of the final list (nums1))
3. else set nums1[k] to nums2[j] and decrement
j
(case where nums2[j] is either larger or
smaller than nums1[i], fills in middle slots
or end slots)
4. continue decrementing k
(loop should end before k < 0)
"""
def merge_2(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(merge(nums1,m,nums2,n))

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(merge(nums1,m,nums2,n))

    nums1 = [4,0,0,0,0,0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5
    print(merge(nums1,m,nums2,n))

