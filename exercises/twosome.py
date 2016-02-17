def two_sum(nums,target):
	
	mydict={}
	for i in range(len(nums)):
		key = target - nums[i]
		#print(nums[i])
		print(key)
		#ind = i
		if(key in mydict):
            
			return [mydict[key],i]
		else:

			#print (i)
			mydict[nums[i]] = i
			print(mydict)
	#count+=1

#print(two_sum([2,5,1,7,3,58,12],14))
print(two_sum([2,5,1,7,78,54,56,32,55,10,200,100],300))