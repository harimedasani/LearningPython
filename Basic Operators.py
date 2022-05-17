# Python Operators Precedence Rule – PEMDAS
# P – Parentheses.
# E – Exponentiation.
# M – Multiplication.
# D – Division.
# A – Addition.
# S – Subtraction.
# Another operator available is the modulo (%) operator
# returns the integer remainder of the division. dividend % divisor = remainder.

square = 7 ** 2
cube = 2 ** 3
print(square)
print(cube)


# problem
# The object() function returns an empty object.
# You cannot add new properties or methods to this object.
# This object is the base for all classes, it holds the built-in properties
# and methods which are default for all classes


x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

