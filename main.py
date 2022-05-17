# printing Hello World
print("Hello World")

# variables and Data Types
# Python is completely object oriented, and not "statically typed".
# The isinstance() function returns True if the specified object is of the specified type, otherwise False
number = 7
decimal = 10.0
string = 'hello'
print(number)
print(decimal)
print(string)
print(string + " " + str(decimal) + " " + str(number))
if string == 'hello' :
    print('String: %s' % string)
if isinstance(decimal, float) and decimal == 10.0:
    print("Float: %f" % decimal)
if isinstance(number, int) and number == 7:
    print("Integer: %d" % number)

# Lists are very similar to arrays.
# They can contain any type of variable, and they can contain as many variables as you wish.
# Lists can also be iterated over in a very simple manner
# Lists can be joined with the addition operators

num = []
strings = []
names = ["John", "Eric", "Jessica"]
num.append(1)
num.append(2)
num.append(3)
strings.append("Hello")
strings.append("World")

second_name = names[1]

print(num)
print(strings)
print("The second name on the names list is %s" % second_name)
print(num + strings + names)

