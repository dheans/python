a=True

while a:
	
	n=int(input("n = :"))
	print("_____________")
	print("matrix perkalian {0}X{0}".format(n))
	print()
	if n ==0:
		a=False
		print("Program Stoped")


	i=1
	while i < n+1:
		print(i,end="")
		j=1	
		while j < n+1:
		
		
#			if i <= j :
#				print("%4.d"%(i*j),end="")
#			elif i >= j:
#				print("%4.d"%(i*j),end="")
#			
#			else:
#				print("-"*4,end="")
			print("%4.d"%(i*j),end="")
			j +=1

		print()
		i +=1
	
