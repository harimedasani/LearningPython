# Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables
# enclosed in a "tuple" (a fixed size list), together with a format string
# which contains normal text together with "argument specifiers",
# special symbols like "%s" and "%d".

name = "hari"
t = 7
print("hello %s it's %d o clock" % (name, t))

# Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)


data = ('John', 'Doe', '$ 53.44')
formatString = 'Hello %s %s. Your current balance is %s'
print(formatString % data)


# String Operations


astring = "Hello world!"
print(astring.index("o"))
print(astring.count('l'))
print(astring[3:7])
print(astring[::-1])
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split(" ")
print(afewwords)

