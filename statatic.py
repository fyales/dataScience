# coding=utf-8
from matplotlib import pyplot as plt

books = ['White Night','Magic Ring','Nania','The shadow Thief','Normal World','China History']
stars = [3.8,3.5,3.6,4.1,3.2,3.7]

xs = [i + 0.1 for i, _ in enumerate(books)]
plt.bar(xs,stars)
plt.ylabel("Award")
plt.title("Reading Books")
plt.xticks([i + 0.5 for i, _ in enumerate(books)],books)

plt.show()

