from math import sqrt

def is_prime(numb):
    i = int(sqrt(numb))
    while i > 1:
        if numb%i == 0:
            return False
        i -= 1
    return True

def nth_prime(n):
	i = 0
	j = 0
	while i <= n:
	    if is_prime(j):
		prime = j
		i += 1
	    j += 1
	return prime
