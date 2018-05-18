import sys
from math import log

if __name__ == '__main__':
	a, b, c, d, e, f, g, h  = [float(x) for x in sys.argv[1:]]
	i = 0 
	#print(sys.argv[1:])
	while log(1 + f) * (1 + i) >= 0.5:

		n = log(1 + f) * c * d * e * 24 / h / g / b / 1000 +  (1 + i) * log(1 + f)
		n = int(round(n))

		j = 0
		for ii in range(1, n+1):
			j += g * b * 13 / e / (1 + f) ** n
		k = a + c * 24 / 1000 * d * n * 13
		i = k / j / h - 1
	
	
	print(k / j)