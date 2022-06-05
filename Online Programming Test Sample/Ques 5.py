def perfect(n):
	sm=0
	for i in range(1,n):
		print(i)
		if n%i==0:
			sm+=i
	return sm==n
