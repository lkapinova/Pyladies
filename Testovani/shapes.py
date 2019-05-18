from math import pi


def ellipse_area(a, b):
    """Given the lengths of the semi-major and semi-minor axes, returns the
    area of the ellipse."""
    return pi * a * b


# jak by to nemelo vypadat, spatne se to testuje
# from math import pi


# def ellipse_area():
#     """Given the lengths of the semi-major and semi-minor axes, prints the
#     area of the ellipse."""
#     a = float(input('lengths of the semi-major axes: '))
#     b = float(input('lengths of the semi-minor axes: '))
#     print('the area is', pi * a * b)