# Problem: Count letters
# Given a string, count the occurence of each letter in the string. Ignore the
# spaces. Output the letters in following format
# <letter> : <count>
# Example
# Input: 'abcaacbbcbcb'
# Output:
# a : 3
# b : 5
# c : 4

def count_letters(s):
    count = {}

    for i in s:
        if i == ' ':
            pass
        elif i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in count:
        print("{} : {}".format(i, count[i]))

if __name__ == '__main__':
    count_letters('Universe')
    count_letters('Hello Hi Howdy!')

