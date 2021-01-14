# Variables

num_of_oranages = 5 #separate multiple words with _

# Function

def calculate_area(): pass

# Class
# Pascal naming convention
# PascalNamingConvention
# ------------------------------
# str
dir(str)

# str.find() Method
help(str.find)

s = 'Universe'

s = 'abcdabcdabcd'

s.find('d')
s.find('d', 5)
s.find('d', 5, 9)


# str.replace() Method
help(str.replace)


# Mutable vs Immutable
Immutable = 'cannot be changed in place'
Mutable = 'can change in place'


# str.format Method
name = 'Frodo'
age = '33'
s = 'Name is {} and age is {}'

s.format(name, age)

s = "Name is {1} and age is {0}" # this changes the order of the parameters


# sorted
s = 'Hello'
sorted(s)
# ['H', 'e', 'l', 'l', 'o']
s = 'Universe'
sorted(s)
# ['U', 'e', 'e', 'i', 'n', 'r', 's', 'v']
# U comes before all of them because caps have lower integer values
# ord('character') = returns the Unicode point for a one-character string
# chr('number') = returns Unicode string of character with ordinal i

