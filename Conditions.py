# Python uses boolean logic to evaluate conditions.
# The boolean values True and False are returned when an expression is compared or evaluated.
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# variable assignment is done using a single equals operator "=",
# whereas comparison between two variables is done using the double equals operator "==".
# The "not equals" operator is marked as "!="

# The "and" and "or" boolean operators allow building complex boolean expressions
# "not" before a boolean expression
print(not False)
print((not False) == False)

name = 'Hari'
age = 22
if name == 'Hari' and age == 22:
    print('correct')
else:
    print('wrong')

# The "in" operator could be used to check
# if a specified object exists within an iterable object container.

l = ['Hari', 'kumar']
if name in l:
    print(name)

# Unlike the double equals operator "==",
# the "is" operator does not match the values of the variables, but the instances themselves

statement = False
another_statement = True
if statement is True:
    print('hi')
elif another_statement is True:
    print('hello')
else:
    print('world')


m = [1,2,3]
n = [1,2,3]
print(m == n)
print(m is n)

