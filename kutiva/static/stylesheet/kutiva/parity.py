def parity(x):
	result = 0
	while x:
		result ^=1
		x &= x-1
	return result
	

print(parity(2200))
