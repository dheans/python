from random import choice

pilihan = ["gunting", "batu", "kertas"]


nyawa = 3

while nyawa > 0:
	ai = choice(pilihan)
	user = input("masukkan pilihan : ")
	hasil = "Menang" if (((user == "gunting") and (ai == "kertas")) or ((user == "batu") and ( ai == "gunting")) or ((user == "kertas") and (ai == "batu"))) else "Draw" if user == ai else "Kalah"
	print ("ai memilih : %s"%ai)
	print("anda memilih : %s"%user)
	print("Anda >>> ",hasil)
	nyawa -=1
	print()
	if nyawa == 0:
		print("program selesai")