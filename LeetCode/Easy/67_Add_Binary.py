"""
67. ADD BINARY
Given two binary strings a and b, return their sum as a binary string.
"""

"""
first solution:
(20ms/61.44%)(13.35MB/72.62%)
brute force
1. add a and b, if zero return 0
2. go digit by digit from the back, if > 1
set carry to True and add d % 2 to l
3. else set carry false and add d
4. at the end if carry, add "1"
5. join in reverse order
"""
def addBinary(a, b):
    c = int(a) + int(b)
    #base case
    if c == 0:
        return "0"
    l = []
    carry = False
    while c > 0:
        #take back int
        d = c % 10
        if carry:
            d = d + 1
        #case for 3 and 2
        if d > 1:
            carry = True
            l.append(str(d % 2))
        #case for 1 and 0
        else:
            carry = False
            l.append(str(d))
        #remove back int
        c = c // 10
    #if there is still a carry needed at the end
    if carry:
        l.append("1")
    return "".join(reversed(l))

"""
second solution:
(15ms/85.25%)(13.37MB/72.62%)
iterate in base 2
1. set a and b to base 2 and add, if zero return "0:
2. convert to binary using ans%2 and ans=ans//2
3. return reversed string
"""
def addBinary_2(a, b):
    a = int(a,2) #converts binary string to base 10
    b = int(b,2)
    ans = a + b
    if(a == 0 and b == 0):
        return "0"
    mod = ""
    #general formula to convert base 10 to binary(in reverse order)
    while(ans >= 1):
        mod += str(int(ans%2))
        ans = ans//2
    return mod[::-1] #reverses string

if __name__ == "__main__":
    a = "11"
    b = "1"
    print(addBinary(a,b))
    a2 = "1010"
    b2 = "1011"
    print(addBinary(a2,b2))