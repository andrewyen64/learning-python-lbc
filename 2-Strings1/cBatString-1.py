# Provided by codingbat.com/python/Strings-1

def hello_name(name):
  return 'Hello ' + name + '!'

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

def make_out_word(out, word):
  half = len(out) / 2
  return (out[:half] + word + out[half:])
  
def extra_end(str):
  a = str[-2:]
  return (a+a+a)

def first_two(str):
  return str [0:2]

def first_half(str):
  half = len(str) // 2
  return str[:half]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  if len(a) < len(b):
    short = a
    long = b
  else:
    short = b
    long = a
  return short + long + short

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  return str[2:] + str[:2]
