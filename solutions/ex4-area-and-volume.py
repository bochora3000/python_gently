"""
area(10, 4)  →  40
perimeter(10, 4)  →  28
volume(10, 4, 5)  →  200
surface_area(10, 4, 5)  →  220

Area, perimeter, volume, and surface area are straightforward calculations. This exercise is similar to Exercise #2, “Temperature Conversion” and Exercise #3, “Odd & Even.” Each function in this exercise is a simple calculation and return statement. However, area and volume are slightly more complicated because they involve multiple parameters. This exercise continues to challenge you to translate mathematical formulas into Python code.

Exercise Description

You will write four functions for this exercise. The functions area() and perimeter() have length and width parameters and the functions volume() and surface_area() have length, width, and height parameters. These functions return the area, perimeter, volume, and surface area, respectively.

The formulas for calculating area, perimeter, volume, and surface area are based on the length (L), width (W), and height (H) of the shape:






Area is a two-dimensional measurement from multiplying length and width. Perimeter is the sum of all of the four one-dimensional lines around the rectangle. Volume is a three-dimensional measurement from multiplying length, width, and height. Surface area is the sum of all six of the two-dimensional areas around the cube. Each of these areas comes from multiplying two of the three length, width, or height dimensions.

"""


def area(length, width):
    #    ·       area = L × W
    return length * width


def perimeter(length, width):
    # ·       perimeter = L + W + L + W
    return (length + width) * 2


def volume(length, width, height):
    # ·       volume = L × W × H
    return length * width * height


def surface_area(length, width, height):
    # ·       surface area = (L × W × 2) + (L × H × 2) + (W × H × 2)
    return (length * width * 2) + (length * height * 2) + (width * height * 2)


assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340
