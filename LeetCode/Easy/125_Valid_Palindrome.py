"""
125. VALID PALINDROME
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

"""
first solution:
(30ms/71.40%)(14.95MB/45.69%)
index comparison
1. remove spaces and set lowercase
2. remove non-alphanumeric chars
3. iterate to midpoint checking front
and back chars for similarity
"""


def isPalindrome(s):
    s = s.strip(" ").lower()
    s = "".join(filter(str.isalnum, str(s)))
    for i in range(len(s) >> 2 - 1):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


"""
second solution:
(24ms/88.48%)(16.28MB/10.15%)
condensed version
1. remove spaces and set lowercase for
all non-alphanumeric chars
3. iterate to midpoint checking front
and back chars for similarity
"""


def isPalindrome_2(s):
    # removes spaces, non-alphanumeric and sets lower
    s = [c.lower() for c in s if c.isalnum()]
    # ~i is -i-1 aka opposing char
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
