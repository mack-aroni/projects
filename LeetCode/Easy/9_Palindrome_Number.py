import math

"""
9. PALINDROME NUMBER
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""

"""
first solution
not using strings
1. eliminate base cases (0, neg)
2. use math.log10 to get magnitude of int
3. compare ints from back to front while
eliminating front and back ints as we go
"""
def isPalindrome(x):
    if (x == 0):
        return True
    if (x < 0):
        return False
    f = int(math.log10(x))
    while x > 0:
        if (x // 10**f) != (x % 10**1):
            return False
        x = (x - (x // 10**f) * 10**f)
        x //= 10
        f = f - 2
    return True

"""
second solution
reverse int and compare
"""
def isPalindrome_2(self, x):
        if x < 0:
            return False
        reversed_num = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
        return reversed_num == x

if __name__ == "__main__":
    print(isPalindrome(12))
    print(isPalindrome(101))
    print(isPalindrome(3425243))