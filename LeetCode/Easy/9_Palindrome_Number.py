import math

"""
9. PALINDROME NUMBER
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""

"""
first solution
(54ms/49.31%)(13.5MB/6.56%)
not using strings
1. eliminate base cases (0, neg)
2. use math.log10 to get magnitude of int
3. compare ints from back to front using

"""
def isPalindrome(x):
    if (x == 0):
        return True
    if (x < 0):
        return False
    f = int(math.log10(x)) #front pointer
    b = 0 #end pointer
    while f > b:
        if (x // 10**f) != (x % 10**(b+1) // 10**b):
            return False
        x = x - (x // 10**f) * 10**f #remove top int of x
        f = f - 1 
        b = b + 1
    return True

"""
second solution
(63ms/28.85%)(13.2MB/85.59%)
reverse int and compare
"""
def isPalindrome_2(self, x):
        if x < 0:
            return False
        reversed_num = 0
        temp = x
        while temp != 0:
            digit = temp % 10 #take last int
            reversed_num = reversed_num * 10 + digit #add to front of reversed
            temp //= 10 # remove last int
        return reversed_num == x

if __name__ == "__main__":
    print(isPalindrome(12))
    print(isPalindrome(101))
    print(isPalindrome(3425243))