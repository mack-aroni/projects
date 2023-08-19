"""
20. VALID PARENTHESES
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

"""
first solution:
(11ms/91.26%)(13.6MB/19.12%)
using a stack
1. eliminate base case of len(s) == 1
2. if forward brackets, add opposite to stack
3. if backward brackets, if equal to stack[-1],
pop from stack, otherwise return False
4. at the end return if the stack is empty
"""
def isValid(s):
    if len(s) == 1:
        return False
    stack = []
    for i in range(len(s)):
        #cases for forward brackets
        if s[i] == "(":
            stack.append(")")
        elif s[i] == "[":
            stack.append("]")
        elif s[i] == "{":
            stack.append("}")
        #cases for reverse
        elif s[i] == ")" or s[i] == "]" or s[i] == "}":
            #no accompanying forward bracket
            if len(stack) == 0:
                return False
            if stack[-1] == s[i]:
                stack.pop()
            #no accompanying forward bracket
            else:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    s = "([)]"
    print(isValid(s))
    s1 = "{[]}"
    print(isValid(s1))
    s2 = "(])"
    print(isValid(s2))