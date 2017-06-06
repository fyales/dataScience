# for division of division
from __future__ import division
# first of all,hello python
print("hello world")

# base
print 5 / 2
print 5 // 2\

# function
def double(x):
	return x * 2
print double(10)

# Exception
try:
	print 0 / 0
except ZeroDivisionError:
	print 'cannot divide by zero'

# List
countries = ['China','USA','Japan']
for country in countries:
	print country

# Tuple
provinces = ('JiangSu','ShangHai','BeJing')
for province in provinces:
	print province

# Dictionary
person = {'name':'fyales','age':26}
for i in person:
	print person[i]



