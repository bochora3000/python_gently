# is_odd(13)  →  True
# is_even(13)  →  False

# Determining if a number is even or odd is a common calculation that uses the modulo operator. Like Exercise #2, “Temperature Conversion,” the functions for this exercise’s solution functions can be as little as one line long.

# This exercise covers the % modulo operator, and the technique of using modulo-2 arithmetic to determine if a number is even or odd.

# Exercise Description

# Write two functions, is_odd() and is_even(), with a single numeric parameter named number. The is_odd() function returns True if number is odd and False if number is even. The is_even() function returns the True if number is even and False if number is odd. Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered an even number.

def is_odd(number):
    if isinstance(number, int):
        return number % 2 != 0
    return False


def is_even(number):
    if isinstance(number, int):
        return number % 2 == 0
    return False


assert is_odd(42) == False

assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False
