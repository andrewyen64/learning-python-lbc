# Problem: Count Letters - Reverse Sorted
# Given a string, count the occurence of each letter in the string. Ignore the
# spaces. Print the letters in descending order of occurences
# <letter> : <count>
# Example
# Input: 'abcaacbbcbcb'
# Output:
# b : 5
# c : 4
# a : 3

import operator

def count_letters(s):
    count = {}

    for i in s:
        if i == ' ':
            pass
        elif i in count:
            count[i] += 1
        else:
            count[i] = 1

    sorted_count = dict(sorted(count.items(), key=operator.itemgetter(1), reverse=True))

    for i in sorted_count:
        print("{} : {}".format(i, sorted_count[i]))

if __name__ == '__main__':
    count_letters('Universe')
    count_letters('Hello Hi Howdy!')