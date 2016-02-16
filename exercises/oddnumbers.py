def oddnumbers(a,b):
	sums = []
	if a >= b:
		print (""+str(a)+ " is larger than "+str(b))
		return 0

	for i in range(a,b):
		if i % 2 != 0:
			print (i)
			sums.append(i)
		
	return sums

oddnumbers(1,10)