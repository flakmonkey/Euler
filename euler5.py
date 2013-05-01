def find_gcd(a,b):
	while a != 0 and b != 0:
		if a > b:
			a -= b
		else:
			b -= a
	if b == 0:
		return a
	else:
		return b

def reduction(a,b):
	reduction = (a * b) / find_gcd(a, b)
	return reduction

gcd = 1

for i in range(1, 21):
	gcd = reduction(gcd, i)

print gcd
