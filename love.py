
print("yes or no")


def love():
	print()
	print("I LOVE YOU ALWAYS")
	
	for row in range(6):
		for col in range (7):
			if(row==0 and col%3 != 0) or(row==1 and col%3==0) or(row-col==2) or(row+col==8):
				print(" ♥️", end="")
			else:
				print("    ", end="")
		print()

def live():
	print()
	print("MY HEART IS HURT!!")
	
	for row in range(6):
		for col in range (7):
			if(row==0 and col%3 != 0) or(row==1 and col%3==0) or(row-col==2) or(row+col==8):
			
				print(" 💔", end="")
			else:
				print("    ", end="")
		print()

while True:
	tex= input("WILL YOU MERRY ME? : y/n")
	
	if tex =="y":
		love()
	
		
	elif tex=="n":
		live()
	else:
		print("\ninsert 'y' or 'n' ")
		break