# membuat game tebak angka

import random

cpu=random.randint(1,10)
i=1

while i:
	ai=int(input("masukan angka 1 sampai 10 : \n"))
	if ai==cpu:
		print("\ntebakan anda benar")
		i=0
	elif ai != cpu and ai<= cpu:
		print("\nangka terlalu kecil\n")
	elif ai!= cpu and ai>= cpu:
		print("\nangka terlalu besar\n")
	