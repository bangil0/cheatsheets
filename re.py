import re

# https://www.tutorialspoint.com/python/python_reg_expressions.htm
  # a|b	Matches either a or b.
  # \w	Matches word characters.
  # \W	Matches nonword characters.
  # \d	Matches digits. Equivalent to [0-9].
  # \D	Matches nondigits.

phone = "2004-959-559 # This is Phone Number"


# match; output if result at start of string
# search; output first result in string
num = re.search(r'2004', phone)
print num.group()

# findall; output all results in a list
num = re.findall(r'2004|Phone', phone)
print num

# replace
num = re.sub(r'\W', '', phone)  #3 arguments
print num
