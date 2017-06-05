import random
# yield 
def fab(max):
	n,a,b = 0,0,1
	while n < max :
		yield b
		print b
		a,b = b,a + b
		n = n + 1

f = fab(5)
f.next()
f.next()
f.next()
f.next()
f.next()

# random
four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms