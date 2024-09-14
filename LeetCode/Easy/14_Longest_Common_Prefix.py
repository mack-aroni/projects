"""
14. LONGEST COMMON PREFIX
Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
first solution:
(20ms/52.90%)(13.2MB/99.83%)
brute force
1. take smallest str length
2. iterate over each str index from 0 to l
3. if equal add to pre, else break
"""


def longestCommonPrefix(strs):
    # break strings into lengths and takes min
    l = min(map(lambda s: len(s), strs))
    pre = ""
    # each string from 0-l
    for i in range(l):
        x = True
        # check each string with index i
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
(18ms/66.24%)(13.62MB/18.01%)
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
    # find min string length of first and last
    for i in range(min(len(first), len(last))):
        # compare those two strings
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
