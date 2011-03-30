def esPrimo(i):
	aux=True
	ls=range(2,i)
	for j in ls:
		d=(float(i)/float(j))
		s= (i/j)
		if d%s == 0.0:
			aux=False
	return aux
def primos(n):
	ls=range(1,n)
	if n==1:
		print 1,
	for i in ls:
		if esPrimo(i):
			print i,

