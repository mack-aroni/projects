"""
66. PLUS ONE
You are given a large integer represented as an
integer array digits, where each digits[i] is the
ith digit of the integer. The digits are ordered
from most significant to least significant in
left-to-right order. The large integer does not
contain any leading 0's.

Increment the large integer by one and return
the resulting array of digits.
"""

"""
first solution:
brute force
(6ms/99.41%)(13.13MB/91.24%)
1. iterate from back of digits
2. add one and determine if carry is necessary
3. if so move forward and add 1, repeat
4. if the first index needs a carry, insert 0 in front
"""


def plusOne(digits):
    carry = True
    for i in reversed(range(0, len(digits))):
        print(i, digits[i], carry)
        if carry:
            if digits[i] + 1 > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] = digits[i] + 1
                carry = False
        else:
            break
    return digits


if __name__ == "__main__":
    digits = [1, 2, 3]
    print(plusOne(digits))
    digits2 = [1, 9, 8, 9]
    print(plusOne(digits2))
    digits3 = [9]
    print(plusOne(digits3))
