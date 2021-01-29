### Lists and Tuples
# - C++ array of pointers
# - ordered collection, sequence
# - mutable, any type, any length

# Lists use square brackets [] and are mutable
# Tuples use parenthese () and are immutable

['Mars', 3.14, 1000]
# ['Mars', 3.14, 1000]
list('Saturn')
# ['S', 'a', 't', 'u', 'r', 'n']
list(range(5, 100, 5))
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[100] * 5
# [100, 100, 100, 100, 100]

## Indexing --------------------------------------------------------------------
list('Saturn')
# ['S', 'a', 't', 'u', 'r', 'n']
list(range(5, 100, 5))
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[100] * 5
# [100, 100, 100, 100, 100]
L = ['Mars', 3.14, 1000]
L[0]
# 'Mars'
L[0][-1]
# 's'

# In membership
L = ['Mars', 3.14, 5000]
5000 in L # True
5001 in L # False

for item in L:
    print(item * 10) 
# MarsMarsMarsMarsMarsMarsMarsMarsMarsMars
# 31.400000000000002
# 50000

for item in range(len(L)):
    print(L[item])
# Mars
# 3.14
# 5000

# Return true if 1st and last element are same
def end_symmetric(arr):
    return arr[0] == arr[-1]
print(end_symmetric(['Mars', 3.14, 5000])) # False
print(end_symmetric(['Mars', 3.14, 'Mars'])) # True

M = [[1,2,3], [4,5,6], [7,8,9]]
M[0] # [1, 2, 3]
M[1] # [4, 5, 6]
M[2] # [7, 8, 9]
M[1][1] # 5

for row in M:
    print(M[0])
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
for x in M:
    print(x)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

## Sorting / Custom Sorting --------------------------------------------
s = 'Eric'
sorted(s)
# ['E', 'c', 'i', 'r']

L1 = [1000, 'Mars', 3.14]
sorted(L1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'str' and 'int'
#       => Can't sort 2 different variable types

L = [1000, 500, 2, 9999]
# A custom key function can be supplied to customize the sort order, 
# and the reverse flag can be set to request the result in descending order.
sorted(L, reverse=True) 
# [9999, 1000, 500, 2]

names = ['aaaa', 'b', 'ccc', 'dd']
#          4      1     3     2
print(sorted(names, key=len)) # ['b', 'dd', 'ccc', 'aaaa']
print(sorted(names, key=len, reverse=True)) # ['aaaa', 'ccc', 'dd', 'b']


names = ['aaaa', 'bz', 'cccx', 'ddy']
print(sorted(names))
print(sorted(names, key=len))

# Sort the strings based on last character of string
def last(s): return s[-1]

print(sorted(names, key=last))
# ['aaaa', 'cccx', 'ddy', 'bz']


names = ['aaaa', 'Aaad', 'ccs', 'eq']
def change_to_lower(s):
    return s.lower()

sorted(names)
# ['Aaad', 'aaaa', 'ccs', 'eq']
sorted(names, key=change_to_lower)
# ['aaaa', 'Aaad', 'ccs', 'eq']


## Includes --------------------------
# You can use 'element in arr' to check if element is included in the array
# Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
    return 2 in nums or 3 in nums