"""
14. LONGEST COMMON PREFIX
Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
first solution:
brute force
1. take smallest str length
2. iterate over each str index from 0 to l
3. if equal add to pre, else break
"""
def longestCommonPrefix(strs):
    l = min(map(lambda s: len(s), strs))
    print(l)
    pre = ""
    for i in range(l):
        x = True
        for s in range(len(strs)):
            if strs[s][i] != strs[0][i]:
                x = False
        if x:
            pre = pre + strs[0][i]
        else:
            break
    return pre

"""
second solution:
lexicographic sort
1. sort strs lexicographically (alphabetically)
2. compare first and last strings
3. if they have the same indexes add to pre else return
"""
def longestCommonPrefix_2(strs):
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans 

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
