### Dictionaries, Sets, and Files - 2

## Sets --------------------------------------------------
# - a collection of distinct items {val1, val2,... valn}

s = set()
s
# set()
s = set('andrew yen')
s
# {'r', 'e', ' ', 'y', 'n', 'w', 'd', 'a'}

s = {}
s.add(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'add'
s = set()
s = {1, 3, 5}
s.add(6)
s
# {1, 3, 5, 6}

# intersection = when a value is in 2 sets
tennis = {'a', 'b', 'c', 'x', 'y', 'z'}
baseball = {'a', 'd', 'e', 'x', 'y', 'o'}
# In this case, ('a', 'x', 'y')

s1 = {1, 3, 5, 10}
s2 = {1, 4, 9, 5}
# `&` and s1.intersection(s2) return the intersections
s1 & s2 
# {1, 5}
s1.intersection(s2)
# {1, 5}

# `|` or s1.union(s2) combine sets
s1 | s2 
s1.union(s2)
# {1, 3, 4, 5, 9, 10}

s1 - s2  # Returns the difference of 2 or more sets as a new set
# {10, 3}
s1.difference(s2)
# {10, 3}


## Files -----------------------------------------
# - read
# - write -> create/overwrite
        # -> append

## open('path/to/file', mode) -------------------
open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/unique_chars.py')
f = open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/unique_chars.py', 'r')
# f -> read
#   -> write
#   -> append
f.read()

f1 = open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/unique_chars.py', 'r')
lines = f1.readlines()

for x in lines:
    print(x, end = '')
# # Problem: Is Unique

# Write a method name unique_chars which accepts a string as input parameters

# Function returns true if string contains all unique characters

# Else it will return False...

for x in lines:
    print(x, end = '')  # end = '' gets rid of extra space from above example
# Problem: Is Unique
# Write a method name unique_chars which accepts a string as input parameters
# Function returns true if string contains all unique characters
# Else it will return False...


## f.write ----------------
f = open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/unique_chars.py', 'w')
f.write("My name is Blank")
f.write("I eat everyday")

f.close()

f = open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/unique_chars.py', 'w')
f.write('Writing again\n')


input = open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/unique_chars.py', 'r')
output = open('/Users/Andrew/Desktop/letsBrewCode/letsbrewcode-python/9-DictsSetsFiles-2/myfile.txt', 'w')

for line in input:
    output.write(line)
    output.write('!@#$%^&*()')

output.close()
