import time



nama ="User"
pwd="User123"
def clon(x):
	return time.strftime(x)


class User:
	def __init__(self, nama=None,pwd=None):
		self.__nama = nama
		self.__pwd = pwd
	def Log_in(self):
		Online = True
		ai="Bot >\n\t"
		us="User >\n\t"
		print(ai,"What can i do for you ?")
		while Online:
			co=input(us).split(" ")
			
			if "tanggal" in co:
				i="%d"

				print(ai,"\tSekarang Tanggal ",clon(i))
			elif "bulan" in co:
				i="%B"
				print(ai,"\tSekarang Bulan ",clon(i))
			elif "hari" in co:
				i="%A"
				print(ai,"\tHari ini hari ",clon(i))
			elif "tahun" in co:
				i="%Y"
				print(ai,"\tSekarang Tahun",clon(i))
			elif "exit" in co:
				print(ai,"\tBye, Salam Bot Sederhana")
				Online = False
			else:
				print(ai,"\tMaaf Bot masih baru,\n\tBELUM PAHAM ARTI {}".format(" ".join(co)))
			
		
		
	def __repr__(self):
		return f"Welcome {self.__nama}"
	
Log_Out = True
cois=3
while Log_Out:
	user=input("[?]_Nama : ")
	pas=input("[?]_Password : ")
	print()
	if user == nama and pas == pwd:
		User=User(user,pas)
		Log_Out = False
		print(User)
		User.Log_in()
	elif user != nama and pas != pwd :
		print(f"Nama {user} dan {pas} Belum Terdaftar\n")
		cois -=1
	elif pas != pwd:
		print("Password Salah\n")
		cois -=1
	elif user != nama:
		print(f"Nama Anda {user} Tidak Cocok\n")
		cois -=1
	if cois == 0:
		print("\nMaaf\nKesempatan Anda Habis\nSilahkan Register")
		Log_Out = False


	
	
	
		
		
