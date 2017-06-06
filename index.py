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

# Control Stream
print('It is Control Stream Demo')
if 1 < 2 :
    print('Normal World')
elif 1 == 2 :
    print('Evil')
else :
    print('Weird World')


for x in range(0,10):
    print(x)

j = 0
while j < 10 :
    print(j)
    j += 1
    
# boolean grammar
# Python use 'None' as a value which don't exist

# List Comprehension
evenNumbers = [x for x in range(0,5) if x % 2 == 0]
evenNumber = 0
for evenNumber in evenNumbers:
    print(evenNumber)


