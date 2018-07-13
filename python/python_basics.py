# STRING FORMAT
#--------------------------------
# more: https://mkaz.tech/code/python-string-format-cookbook/
print 'this score is {}'.format(1.1234)
'this score is 1.1234'
print 'this score is {:.2f}'.format(1.1234) # 2 decimal format
'this score is 1.12'

# 0 PADDING
test = '1'
test.zfill(5)
'00001'


# LOOPS
#--------------------------------
# enumerate
a = [10,123,1231,232143434,234235]
for num, i in enumerate(a):
    print num, i

0 10
1 123
2 1231
3 232143434
4 234235

# can change the start number
for num, i in enumerate(a, 1):
    print num, i

1 10
2 123
3 1231
4 232143434
5 234235

# LIST SLICING
#--------------------------------
list1[-1] # get last in the list
list1[::20] # get every 20th feature
list1[::-1] # reverse sort the entire list
list1[::,0] # for a nested list, grab first value

# append
x = [1, 2, 3]
x.append([4, 5])
print (x)
>>>[1, 2, 3, [4, 5]]

# extend
x = [1, 2, 3]
x.extend([4, 5])
print (x)
>>>[1, 2, 3, 4, 5]

# sort
list2 = [(1,2),(53,12),(23,232),(99,231)]
def take2nd(elem):
    # for sorting 2nd position of a tuple within a list
    return elem[1]

    # reverse is descending order
    # key is to take position of sort if it is a nested list
sorted(list2, reverse=True, key=take2nd) 

# reverse sort
list1 = [1,2,3,4,5]
print(list1[::-1])
>>> 


# DICTIONARY
#--------------------------------
dictname.items()
# dict_items([('97', 63), ('129', 1), ('134', 2)])
dictname.keys()
# dict_keys(['97', '129', '134'])
dictname.values()
# dict_values([63, 1, 2])

# remove key
dictname.pop('keyName')


# CONCAT
#--------------------------------
s = "-"
seq = ("a", "b", "c")
print (s.join(seq))
# a-b-c


# SORTING
#--------------------------------
sorted(token, reverse=True) # default is ascending, reverse=True is descending
token.reverse() # easier, but it will change the base variable

# there is a key parameter that can select which value in the tuple to be sorted by
sorted(student_tuples, key=lambda x: x[2])
import operator
sorted(btwnCent.items(), key=operator.itemgetter(1), reverse = True)

# JSON
#--------------------------------
sample = {'this': 1, 'this2':3}

import json
with open('result.json', 'w') as fp:
    json.dump(sample,fp)


# DIVISION IN DECIMALS
#--------------------------------
# in python, there is no decimals if you do a division. Use the following to obtain it.
# only for python 2.7
# fixed in python 3>
4 / float(100)
0.04
4 / 100.0
0.04


# DUPLICATES
#--------------------------------
list1 = ['a', 'a', 'b', 'c', 'd', 'd']
len(list1) # 6
len(set(list1)) # 4
print set(list1) # set(['a', 'c', 'b', 'd'])

# remove item
list1.remove('valuename')



# PICKLING
#--------------------------------
# http://www.pitt.edu/~naraehan/python2/pickling.html
# saving your Python data object as itself
# also see https://stackoverflow.com/questions/26860051/how-to-reduce-the-time-taken-to-load-a-pickle-file-in-python
import cPickle

f = open('gradesdict.p', 'rb')
mydict = cPickle.load(f)       
f.close()


# READING FROM ZIP FILE
#--------------------------------



# DATE
#--------------------------------
from datetime import datetime

x = datetime.strptime('2011-01-03', '%Y-%m-%d')
print x
# 2011-01-03 00:00:00
x = datetime.strptime('2011-01-03', '%Y-%m-%d').date()
print x
# 2011-01-03
x = datetime.strptime('2011', '%Y').date()
print x
# 2011-01-01
d = datetime.strptime("22:30", "%H:%M")
print d.strftime("%I:%M %p")
# '10:30 PM'


import time
# current date
time.strftime("%d/%m/%Y")
# current time in epoch
time.time()

from datetime import datetime, timedelta
print datetime.now()
# 2017-09-05 21:17:02.111204
print datetime.now().date()
# 2017-09-05
print datetime.now() + timedelta(days=5, hours=-5)
# 2017-09-10 16:17:02.419905


# Parsing Time Formats
#----------------------
# dateutil.parser is very good at parsing all times of date formats into standard ones
import dateutil.parser
from datetime import datetime

# note that the default day if not present will be the current day, have to add a manual default to override
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0)).date()
# 2014-02-01

# fuzzy = True ignores any exceptions
print dateutil.parser.parse("2014-02", default=datetime(2017, 1, 1, 0, 0), fuzzy=True).date()


# Set Timezone to Local
#----------------------
from dateutil import tz
# utc = datetime.utcnow()
utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')
# Tell the datetime object that it's in UTC time zone since 
# datetime objects are 'naive' by default
utc = utc.replace(tzinfo=tz.tzutc())
# Convert time zone
central = utc.astimezone(tz.tzlocal())



# TASK SCHEDULER
#--------------------------------
# Go to Task Scheduler
# Create Task
# Give a name
# Under Triggers > Add New > Check Repeat Task > Every 1 Hour or Others > for duration of: Change Indefinitely
# Under Actions > Start a program 
  # > Program/Script (choose python.exe path)
        # C:\ProgramData\Anaconda2\python.exe
  # > Add arguements (choose python script path)
        # "C:\Users\xx\xx\Scripts\MyPythonScripts\facebook_public.py"
  # Note that double quotes needed is there are spaces in path



# EXCEPTION HANDLING
#--------------------------------
import sys
import traceback

try:
    something
except Exception as e:
    print sys.exc_info()[2].tb_lineno # line number where code breaks
    print e # exact item that have issue
    print traceback.format_exc() # full traceback error



# SUBPROCESS
#--------------------------------
# call command prompt in python

import subprocess

subprocess.call(r"""mongoexport --db test-database --collection wsg --type=csv --fieldFile "C:\Users\Teo S\Desktop\fields.txt"
                    --out export.csv""", shell=True)
subprocess.call(["mongoexport", "--db", "test-database", "--collection", "wsg", "--type=csv", "--fieldFile", "fields.txt" ,
                    "--out", "export.csv"])
                    
# output value of 1 means good


# Virtual Environment
#--------------------------------
# https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/

virtualenv env # create a virtual env called env
source env/bin/activate # change python env to work within env
which python # confirm python env is in virtual
deactivate # escape from virtual env


# Local Server
#--------------------------------
python -m SimpleHTTPServer 3000 # python2
python -m http.server 3000 # python3


# PRETTY PRINTS
#--------------------------------

# pretty print json, dictionary etc.
from pprint import pprint
pprint(the_list)


# print a table
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["name", "rank", "gender"]
table.append_row(["Jacob", 1, "boy"])
table.append_row(["Isabella", 1, "girl"])
table.append_row(["Ethan", 2, "boy"])
table.append_row(["Sophia", 2, "girl"])
table.append_row(["Michael", 3, "boy"])
print(table)

+----------+------+--------+
|   name   | rank | gender |
+----------+------+--------+
|  Jacob   |  1   |  boy   |
+----------+------+--------+
| Isabella |  1   |  girl  |
+----------+------+--------+
|  Ethan   |  2   |  boy   |
+----------+------+--------+
|  Sophia  |  2   |  girl  |
+----------+------+--------+
| Michael  |  3   |  boy   |
+----------+------+--------+


# pretty print json
import json

your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
parsed = json.loads(your_json)
print json.dumps(parsed, indent=4, sort_keys=True)


# convert list of images into pdf -------------------------
from fpdf import FPDF
import os

# get list of images file path
path = r'/Users/xx/Desktop/foldername'
[path+'/'+i for i in os.listdir(path)]

pdf = FPDF()
x,y,w,h = 0,0,200,300 # dimensions for A4, might need to adjust accordingly
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")