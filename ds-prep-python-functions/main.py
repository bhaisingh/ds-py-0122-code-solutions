bool_to_int = lambda value: 1 if value else 0
print('bool_to_int(True) ', bool_to_int(True))
print('bool_to_int(False) ', bool_to_int(False))

get_smaller = lambda a, b: a if a < b else b
print('get_smaller(16, 31) ', get_smaller(16, 31))
print('get_smaller(253, 223) ', get_smaller(253, 223))

def cube(base):
    return base ** 3
print('cube(2) ', cube(2))
print('cube(5) ', cube(5))

def absolute_difference(a, b):
    return abs(a - b)
print('absolute_difference(14, 11) ', absolute_difference(14, 11))
print('absolute_difference(13, 40) ', absolute_difference(13, 40))

def squared_difference(a, b):
    return (a - b) ** 2
print('squared_difference(14, 11) ', squared_difference(14, 11))
print('squared_difference(13, 40) ', squared_difference(13, 40))

def hours_to_minutes(hours):
    return hours * 60
print('hours_to_minutes(3.5) ', hours_to_minutes(hours=3.5))
print('hours_to_minutes(12) ', hours_to_minutes(hours=12))

pi = 3.141592653589793
def get_circumference(radius):
    return 2 * pi * radius
print('get_circumference(1) ', get_circumference(radius=1))
print('get_circumference(9.2) ', get_circumference(radius=9.2))

def linear_transform(x, slope, intercept):
    return slope * x + intercept
print('linear_transform(x=5.0, slope=3.0, intercept=-8.5) ', linear_transform(x=5.0, slope=3.0, intercept=-8.5))
print('linear_transform(slope=-2.1, intercept=17.0, x=2.5) ', linear_transform(slope=-2.1, intercept=17.0, x=2.5))

def standardize(x, x_center, scale_size):
    return (x - x_center) / scale_size
print('standardize(x=8.2, x_center=13.8, scale_size=4.83) ', standardize(x=8.2, x_center=13.8, scale_size=4.83))
print('standardize(scale_size=24.63, x=2.89, x_center=-72.831) ', standardize(scale_size=24.63, x=2.89, x_center=-72.831))
