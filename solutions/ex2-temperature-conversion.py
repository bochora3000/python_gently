"""
convert_to_celsius(32)  →  0.0
convert_to_fahrenheit(100)  →  212

Converting between Celsius and Fahrenheit involves a basic calculation and provides a good exercise for writing functions that take in a numeric input and return a numeric output. This exercise tests your ability to use Python’s math operators and translate math equations into Python code.

Exercise Description

Write a convert_to_fahrenheit() function with a degree_celsius parameter. This function returns the number of this temperature in degrees Fahrenheit. Then write a function named convert_to_celsius() with a degree_fahrenheit parameter and returns a number of this temperature in degrees Celsius.

Use these two formulas for converting between Celsius and Fahrenheit:

·       Fahrenheit = Celsius × (9 / 5) + 32

·       Celsius = (Fahrenheit - 32) × (5 / 9)

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert convert_to_celsius(0) == -17.77777777777778
assert convert_to_celsius(180) == 82.22222222222223
assert convert_to_fahrenheit(0) == 32
assert convert_to_fahrenheit(100) == 212
assert convert_to_celsius(convert_to_fahrenheit(15)) == 15


# Rounding errors cause a slight discrepancy:

assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: math operators
"""


def convert_to_celsius(degree_fahrenheit):
    # Celsius = (Fahrenheit - 32) × (5 / 9)
    return (degree_fahrenheit - 32) * (5/9)


def convert_to_fahrenheit(degree_celsius):
    # Fahrenheit = Celsius × (9 / 5) + 32
    return degree_celsius * (9 / 5) + 32


assert convert_to_celsius(0) == -17.77777777777778
assert convert_to_celsius(180) == 82.22222222222223
assert convert_to_fahrenheit(0) == 32
assert convert_to_fahrenheit(100) == 212
assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
