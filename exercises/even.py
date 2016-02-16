def evennumbers(a,b):
	 sums = []
	for i in range(a,b):
		if(i % 2== 0):
		    print (i)
		    sums[i] = i
	return sums


evennumbers(31,25)