sumSquares = 0
for i in range(1,101):
    sumSquares += i**2

squareSums = sum(range(1,101))**2

print squareSums - sumSquares
