### Python Functions - Part 1
# - argument unpacking
# - defining function
# - scopes

## Argument Unpacking -----------------------------------

x, y = 1, 2, 3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 2) <--

x, y, z = ['frodo', 'sam']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2) <--


# `*` next to a variable ------------------

x, *y = [1, 2, 3, 4, 5]
x # 1
y # [2, 3, 4, 5]

x, *y, z = 'Saturn'
x # 'S'
y # ['a', 't', 'u', 'r']
z # 'n'


## Defining a Function --------------------

def greet(name):
    '''This function will greet. If name is empty then no greeting!'''
    if not name: return
    return 'Hello ' + name + '!'

print(greet('Sam'))
help(greet)

# Automatic Polymorphism --------------------

def multiply(x, y):
    return x * y

print(multiply(2.3, 4))
# 9.2
print(multiply('Hello', 4))
# HelloHelloHelloHello
print(multiply('Hello', 'a'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in multiply
# TypeError: can't multiply sequence by non-int of type 'str'

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

print(intersect([1,2,3,4,5,6,7], [2,4,6,9]))
# [2, 4, 6]
print(intersect(['s', 'a', 't'], 'sharma'))
# ['s', 'a']


time = 'am'

if time == 'am':
    def greet():
        return 'Good morning'
else:
    def greet():
        return 'Good afternoon'

print(greet())
# ----------------------------------------
def func1():
    print('In function1')

    def func2():
        print('This is function 2')

    #funct2()
    print('Ending function 1')
    return func2

x = func1()
x()



