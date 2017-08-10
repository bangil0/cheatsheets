# STRING FORMAT
# more: https://mkaz.tech/code/python-string-format-cookbook/
print 'this score is {}'.format(1.1234)
>>> 'this score is 1.1234'
print 'this score is {:.2f}'.format(1.1234) # 2 decimal format
>>> 'this score is 1.12'


# DIVISION IN DECIMALS
# in python, there is no decimals if you do a division. Use the following to obtain it.
>>> 4 / float(100)
0.04
>>> 4 / 100.0
0.04