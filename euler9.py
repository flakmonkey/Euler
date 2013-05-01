from math import sqrt

def find_c(a, b):
	func = sqrt((a**2 - b**2)**2+(2*a*b)**2)
	return func

def triangle(a,b):
		flt_c = find_c(a,b)
		c = int(sqrt(flt_c))
		if flt_c == c**2:
			return (a,b,c)
		else:
			return None

for a in range(1,1000):
	for b in range(1,1000):
		temp = triangle(a,b)
		if temp:
			if (temp[0] + temp[1] + temp[2]) == 1000:
				print temp
