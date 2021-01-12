# Return Initials
def initials(fname, lname):
    return fname[0] + lname[0]

initials('Frodo', 'Baggins')

# Given a string of length 6, insert a
# '-' in the middle

def insert_hyphen(s):
    print (s[0:3] + '-' + s[3:6])
    print (s[:3] + '-' + s[3:])

insert_hyphen('orange')
# -> ora-nge

# Given a string of even length, insert a 
# '-' in the middle
def insert_hyphen2(s):
    half = len(s) // 2
    return s[:half] + "-" + s[half:]

print(insert_hyphen2('universe'))