# https://codingbat.com/prob/p170842

def double_char(str):
    result = ''
    for x in str:
        result += x*2
    
    return result
# double_char('The') → 'TThhee'


def count_hi(str):
    count = 0
    ## Loop to length-1 and access index i and i+1
    ## in the loop.
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
          count += 1
        
    return count
# count_hi('hiHIhi') → 2
# count_hi('hiho not HOHIhi') → 2


def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str)-1):
        if str[i:i+3] == 'cat':
            cat += 1
        elif str[i:i+3] == 'dog':
            dog += 1
    if cat == dog:
        return True
    else:
        return False
# cat_dog('catdog') → True
# cat_dog('catxxdogxxxdog') → False


def count_code(str):
    count = 0
    for i in range(len(str)):
        if str[i:i+2] == 'co' and str[i+3:i+4] == 'e':
            count += 1
    return count
# count_code('cozexxcope') → 2

def end_other(a, b):
    if a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()):
        return True
    else:
        return False

# Shorter end_other solution
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))

def xyz_there(str):
    for i in range(len(str)):
        if str[i] != '.' and str[i+1:i+4] == 'xyz':
            return True
    if str[0:3] == "xyz":
        return True
    else:
        return False


