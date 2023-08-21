"""
28. INDEX OF FIRST OCCURENCE IN A STRING
Given two strings needle and haystack, return the index
of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""

"""
first solution:
(13ms/76.23%)(13.53MB/18.74%)
brute force
1. check intial case if needle > haystack
2. iterate over haystack from pointer c to len
3. check if haystack[i] == needle[j], if equal
set index if j == 0 and index j and i
4. else break and increment pointer c
5. if j reaches len(needle), return index
6. else return -1 if needle isnt in haystack
"""
def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    index = 0
    # from 0-len
    for c in range(len(haystack)):
        j = 0
        # from c-len
        for i in range(c,len(haystack)):  
            #print("c:",c,"hay:",haystack[i],"need:",needle[j],"j:",j,"index:",index)
            #check until !=, then break, else return index
            if haystack[i] == needle[j]:
                if j == 0:
                    index = i
                j = j + 1
            else:
                break
            if j == len(needle):
                return index
    return -1

"""
second solution:
(12ms/82.30%)(13.4MB/49.43%)
KMP algorithm
"""
def strStr_2(haystack, needle):
    lps = [0] * len(needle)
    pre = 0
    for i in range(1, len(needle)):
        while (pre > 0 and needle[i] != needle[pre]):
            pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre
    n = 0
    for h in range(len(haystack)):
        while (n > 0 and needle[n] != haystack[h]):
            n = lps[n-1]
        if needle[n] == haystack[h]:
            n += 1
        if n == len(needle):
            return h - n + 1
    return -1

if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    #print(strStr(haystack,needle))
    haystack1 = "leetcode"
    needle1 = "leeto"
    #print(strStr(haystack1,needle1))
    haystack2 = "hello"
    needle2 = "ll"
    #print(strStr(haystack2,needle2))
    haystack5 = "aabaabbbaabbbbabaaab"
    needle5 = "abaa"
    print(strStr(haystack5,needle5))
