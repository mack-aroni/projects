"""
242. VALID ANAGRAM
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase, typically
using all the original letters exactly once.
"""

"""
first solution:
(33ms/73.54%)(13.87MB/66.80%)
dictify and compare
1. add all chars of s into a dict
2. compare chars of t to dict
"""


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    dict = {}
    for c in s:
        dict[c] = dict[c] + 1
    for c in t:
        if c not in dict:
            return False
        else:
            dict[c] = dict[c] - 1
            if dict[c] < 0:
                return False
    return True


"""
second solution:
very slow
1. convert strings into lists and alphanumerically sort
2. compare by popping off of each list
"""


def isAnagram_2(s, t):
    if len(s) != len(t):
        return False
    x = list(s)
    y = list(t)
    x.sort(), y.sort()
    print(x, y)
    while x and y:
        if x.pop() != y.pop():
            return False
    return True


if __name__ == "__main__":
    s = "rat"
    t = "car"
    print(isAnagram(s, t))
