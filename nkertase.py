#membuat game batu gunting kertas



from random import choice

pilihan = ["batu", "gunting", "kertas"]

#menentukan perulangan permainan atau nyawa
nyawa = 3

while nyawa >0:
	nyawa -=1
	user= input("batu/gunting/kertas : ") #mengambil input dari user
	komputer = choice(pilihan)

	hasil = "Menang" if (((user == "batu") and (komputer == "gunting")) or ((user == "gunting") and (komputer == "kertas")) or ((user == "kertas") and (komputer == "batu"))) else "Draw" if user == komputer else "Kalah"
	
	print(f"Anda Memilih {user}\nKomputer memilih {komputer}\n\tStatus anda {hasil}\n")
	print("_" * 29)
	print()
	
	if nyawa ==0:
		print("Game over")
		print("Apakah Mau Main Lagi y/t\n")
		o=input()
		print()
		if o in ("y","Y"):
			nyawa =3
		else :
			print("Bye")
			break
