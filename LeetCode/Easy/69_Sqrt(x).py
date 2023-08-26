"""
69. SQRT(X)
Given a non-negative integer x, return the square root of
x rounded down to the nearest integer. The returned integer
should be non-negative as well.

You must not use any built-in exponent function or operator.
"""

"""
first solution:
(1034ms/20.83%)(13.3MB/52.69%)
brute force
"""
def mySqrt(x):
    i = 1
    while x >= i * i:
        i = i + 1
    return i - 1

"""
second solution:
(23ms/53.96%)(13.43MB/9.57%)
binary search
1. take mid of x and 1, mid is max that sqrt(x) can be
2. if mid * mid < x, left becomes mid, else right is mid
3. repeat until mid * mid == x, return l - 1
"""
def mySqrt_2(x):
    l = 1
    r = x
    while l <= r:
        mid = (l + r)//2 # right shift is more efficient than int division
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1
    return l - 1

if __name__ == "__main__":
    x = 8
    print(mySqrt(x))
    x_1 = 103
    print(mySqrt(x_1))