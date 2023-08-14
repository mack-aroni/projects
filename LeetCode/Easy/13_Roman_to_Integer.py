"""
13. ROMAN TO INTEGER
Given a roman numeral, convert it to an integer.
"""

"""
first solution
1. reads front to back each numeral
2. if it proceeds a larger numeral it
subtracts, otherwise it adds to sum
"""
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            print(i,s[i],dict[s[i]],sum)
            if i < len(s)-1 and dict[s[i]] < dict[s[i+1]]:
                sum = sum - dict[s[i]]
            else:
                sum = sum + dict[s[i]]
        return sum
"""
second solution
1. replace all subtractions with irregular numerals
2. parse into list and sum them
"""
def romanToInt_2(s):
    dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    return sum(map(lambda x: dict[x], s))

if __name__ == "__main__":
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))