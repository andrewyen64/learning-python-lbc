# Problem: Is Unique
# Write a method name unique_chars which accepts a string as input parameters
# Function returns true if string contains all unique characters
# Else it will return False

def unique_chars(input):
    s = set()
    for x in input:
        if x not in s:
            s.add(x)
        else:
            return False
    return True

if __name__ == '__main__':

    sample = ['abcd', 'abcdeb', 'zzy']
    for s in sample:
        print('String', s, ' contains unique characters?', unique_chars(s))

# String abcd  contains unique characters? True
# String abcdeb  contains unique characters? False
# String zzy  contains unique characters? False


def unique_chars2(input):
    return len(set(input)) == len(input)

print(unique_chars2('Saturn'))
print(unique_chars2('Frodo'))