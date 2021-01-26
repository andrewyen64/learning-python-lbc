# Iterators

### iter() ------------
s = 'Saturn'
iter(s)
it1 = iter(s)
it2 = iter(s)

next(it1)
# 'S'
next(it1)
# 'a'
next(it1)
# 't'
next(it2)
# 'S'


### range() ------------------------
range
# <class 'range'>
range(100)
# range(0, 100)
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 10, -2))
# []


### For Loop -----------------------
name = 'Frodo'
for ch in name:
    print(ch)
# F
# r
# o
# d
# o

for ch in name:
    print(ch, end=' ') 
# F r o d o

for num in range(10): print(num, end=' ')
# 0 1 2 3 4 5 6 7 8 9

for num in range(100, 1, -2): print(num, end=' ') 
# 100 98 96 94 92 90 88 86 84 82 80 78 76 74 72 70 68 66 64 62 60 58 56 54 52 
# 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2

s = 'Himanshu'
#    01234567
L = len(s)

for x in range(L):
    if x % 2 == 0:
        print(s[x])

# https://codingbat.com/prob/p170842 - String-2 > double_char
def double_char(str):
    result = ''
    for x in str:
      result += x*2

    return result

### While Loop ---------------------------
# for -> iterates over a collection
# while -> iterates over a boolean condition

## break = stops the loop
## continue = returns the control to the beginning of the while loop

x = 5
y = 10

while x < y:
    print('x:{} is less than y:{}')

while True:
    x = input('Enter a char:')
    if x == 'z':
        break
    if x == 'g':
        continue
    print(x * 10)

# Enter a char:a
# aaaaaaaaaa
# Enter a char:b
# bbbbbbbbbb
# Enter a char:t
# tttttttttt
# Enter a char:g
# Enter a char:s
# ssssssssss
# Enter a char:z
# 

