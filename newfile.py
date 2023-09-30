
x=True
while x :
	d= int(input("Mau perkalian berapa? : "))
	print("°•-.,"*5)
	if d ==0:
		x=False
	else:
	
		for i in range(1,11):
			print(f"{d} X {i} = {d*i}")
		print()
