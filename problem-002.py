sum = 0
fib_mem = {}
def fib(n):
	if n in fib_mem:
		return fib_mem[n]
	else:
		fib_mem[n] = n if n < 2 else fib(n-2) + fib(n-1)
		return fib_mem[n]

n = 0
while fib(n) < 4000000:
	if fib(n) % 2 == 0:
		sum += fib(n)
	n += 1

print sum