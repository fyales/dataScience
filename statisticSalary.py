# coding = utf-8
from matplotlib import pyplot as plt
salary = [0,3000,5000,10000,15000,20000,100000]
count= [15142,26432,35221,15878,8322,3898,983]

xs = [ i + 0.1 for i , _ in enumerate(salary)]
plt.axis([0,7,0,40000])
plt.xticks([i for i , _ in enumerate(salary)],salary)
plt.bar(xs,count)
plt.title('Salary Statistic')
plt.ylabel('Salary pencentage')
plt.xlabel('Salary Count')
plt.show()

def sum(count):
    x = 0
    for s in count:
        x = x + s
    return x

def mean(salary,count):
    x = 0
    for (s,p) in zip(salary,count):
        x = x + s * p
    return x / sum(count)

print mean(salary,count)