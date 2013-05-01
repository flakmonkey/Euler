from math import sqrt

def is_prime(numb):
    i = int(sqrt(numb))
    while i > 1:
        if numb % i == 0:
            return False
        i -= 1
    return True
