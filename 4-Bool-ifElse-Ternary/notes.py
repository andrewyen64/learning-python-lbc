# Write a function that returns true if number passed in is even

def is_even(num):
    return num % 2 == 0

def is_qualified(age, state):
    return age >= 18 and state == 'CA'

print(is_even(99))
print(is_even(100))

print(is_qualified(17, 'CA'))

# ===========================
# if condition:
#     stmt1
#     stmt2
# elif:    (<- else if)
#     stmt3
#     stmt4
# else:
#   stmt5


# ====== FizzBuzz ======
# If number is divisible by:
# 3 -> Fizz
# 5 -> Buzz
# 3 and 5 -> FizzBuzz

def fizzbuzz(num):
    print(num, '-> ', end='')

    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

fizzbuzz(10)

# =================================
def starts_with_vowel(name):
    return name[0] in 'AEIOUaeiou'

print(starts_with_vowel('Adam'))
print(starts_with_vowel('Kate'))

