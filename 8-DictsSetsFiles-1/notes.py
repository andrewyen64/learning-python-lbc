### Dictionaries in Python
# hashmaps, map, associative arrays, 
# key-values (key: value)
# - mutable

D = {1000: 'Something', 2000: 'Something more'}
len(D)
# 2
D[1000] # 'Something'
D[2000] # 'Something more'
D[3000]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 3000

## Use in to return True if it's in dict ----------
3000 in D # False
2000 in D # True


## Adding -----------------------------------------
D = {'USA': 'Washington', 'AUS': 'Canberra'}
D['JPN'] = 'Tokyo'
D
# {'USA': 'Washington', 'AUS': 'Canberra', 'JPN': 'Tokyo'}


## Other Ways to make dicts -------------------
L = [(1, 2), (3, 4), (5, 6)]
dict(L)
# {1: 2, 3: 4, 5: 6}

l1 = [1,2,3,4,5]
l2 = 'Sam'
list(zip(l1, l2))
# [(1, 'S'), (2, 'a'), (3, 'm')]


## items() ------------------------------------
D = {'USA': 'Washington', 'AUS': 'Canberra', 'JPN': 'Tokyo'}
D.items()
# dict_items([('USA', 'Washington'), ('AUS', 'Canberra'), ('JPN', 'Tokyo')])
list(D.items())
# [('USA', 'Washington'), ('AUS', 'Canberra'), ('JPN', 'Tokyo')]

D = {'USA': 'Washington', 'JPN': 'Tokyo'}
for k in D:
    print(k, ' -> ', D[k])
# USA  ->  Washington
# JPN  ->  Tokyo

list(enumerate(D))
# [(0, 'USA'), (1, 'JPN')]

s = 'My name is Han Solo!'
chars = {}
for x in s:
    chars[x] += 1

for x in s:
     if x not in chars:
             chars[x] = 1
     else:
             chars[x] += 1
 
for k in chars:
    print("{} -> {}".format(k, chars[k]))
 
# M -> 1
# y -> 1
#   -> 4
# n -> 2
# a -> 2
# m -> 1
# e -> 1
# i -> 1
# s -> 1
# H -> 1
# S -> 1
# o -> 2
# l -> 1
# ! -> 1
