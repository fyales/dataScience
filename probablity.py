# coding=utf-8
import random

def random_kid():
    return random.choice(['boy','girl'])

random.seed(0)
both_girl = 0
single_girl_single_boy = 0
both_boy = 0
num = 1000000
numFloat = 1000000.00
for i in range(num):
    young = random_kid()
    older = random_kid()
    if older == 'boy' and young == 'boy':
        both_boy += 1
    elif older == 'boy' and young == 'girl':
        single_girl_single_boy += 1
    elif older == 'girl' and young == 'boy':
        single_girl_single_boy += 1
    else:
        both_girl += 1

print("Both is girl",both_girl / numFloat)
print("One is boy ,another is girl",single_girl_single_boy / numFloat)
print("Both is boy",both_boy / numFloat)
