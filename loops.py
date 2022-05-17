# for loop is used iterate over a given sequence
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)

# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
# The difference between range and xrange is that the range function returns a new list
# with numbers of that specified range, whereas xrange returns an iterator, which is more efficient.
for x in range(5):
    print(x)
for x in range(3, 7):
    print(x)
print('hi')
for x in range(3, 10, 3):
    print(x)

# While loops repeat as long as a certain boolean condition is met

count = 0
while count < 5:
    print(count)
    count = count + 1

# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block.
print('break')
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)

# Unlike languages like C,CPP.. we can use else for loops.
# When the loop condition of "for" or "while" statement fails then code part in "else" is executed.

coun = 0
while coun < 5:
    print(coun)
    coun += 1
else:
    print("count value reached %d" % coun)

# Prints out 1,2,3,4
for j in range(1, 10):
    if j % 5 == 0:
        break
    print(j)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
