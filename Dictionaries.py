# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
# Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

names = {}
names[1] = 'Pavan'
names[2] = 'Sarath'
names[3] = 'Hari'
# or names ={1:'Pavan', 2:'Sarath', 3:'Hari'}
print(names)

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list.
# However, a dictionary, unlike a list, does not keep the order of the values stored in it.

for number,name in names.items():
    print('The number %d and name is %s' %(number,name))

# Removing a value
# To remove a specified index we can use del or pop
del names[3]
names.pop(2)
print(names)
