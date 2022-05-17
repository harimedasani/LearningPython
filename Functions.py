# Functions are a convenient way to divide your code into useful blocks,
# allowing us to order our code, make it more readable, reuse it and save some time.
# Also functions are a key way to define interfaces so programmers can share their code
def my_function():
    print("Hello From My Function!")


my_function()


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


my_function_with_args('hari', 'welcome')


# Functions may return a value to the caller, using the keyword- 'return

def summ(a, b):
    return a + b


t = summ(2, 3)
print(t)


