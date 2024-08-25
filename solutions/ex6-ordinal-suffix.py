"""
ordinal_suffix(42)  →  '42nd'

While cardinal numbers refer to the size of a group of objects like “four apples” or “1, 000 tickets”, ordinal numbers refer to the place of an object in an ordered sequence like “first place” or “30th birthday”. This exercise involves numbers but is more an exercise in processing text than doing math.

Exercise Description

In English, ordinal numerals have suffixes such as the “th” in “30th” or “nd” in “2nd”. Write an ordinal_suffix() function with an integer parameter named number and returns a string of the number with its ordinal suffix. For example, ordinal_suffix(42) should return the string '42nd'.

You may use Python’s str() function to convert the integer argument to a string. Python’s endswith() string method could be useful for this exercise, but to maintain the challenge in this exercise, don’t use it as part of your solution.

"""


def ordinal_suffix(num):
    num = str(num)

    if num[-2:] in ('11', '12', '13'):
        return num + 'th'
    elif num[-1] == '1':
        return num + 'st'
    elif num[-1] == '2':
        return num + 'nd'
    elif num[-1] == '3':
        return num + 'rd'
    else:
        return num + 'th'


assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'
