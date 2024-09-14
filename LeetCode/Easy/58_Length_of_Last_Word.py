"""
58. LENGTH OF LAST WORD
Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of
non-space characters only.
"""

"""
first solution:
(8ms/94.40%)(13.76MB/10.10%)
reverse counting
1. iterate from back of string
2. ignore end space, count chars, break
after next space
"""


def lengthOfLastWord(s):
    count = 0
    for i in reversed(range(len(s))):
        if s[i] != " ":
            count = count + 1
        elif count != 0:
            break
    return count


"""
second solution:
(11ms/86.46%)(13.43MB/72.45%)
string trimming
1. trim the string to remove leading and trailing
spaces
2. find the last index of the space character ' '
in the trimmed string
3. if there is no space in the trimmed string, the
last substring is the entire string, so return len
4. if there is a space in the trimmed string, calculate
the length of the last substring from the last space index
to the end of the trimmed string
"""


def lengthOfLastWord_2(self, s):
    s = s.strip()
    last_space_index = s.rfind(" ")

    if last_space_index == -1:
        return len(s)

    return len(s) - last_space_index - 1


if __name__ == "__main__":
    s = "Hello World"
    print(lengthOfLastWord(s))
    s2 = "   fly me   to   the moon  "
    print(lengthOfLastWord(s2))
    s3 = "luffy is still joyboy"
    print(lengthOfLastWord(s3))
