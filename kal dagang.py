
import sys , time

kode=[]
pesanan={"Dada":15000,"Paha":20000,"Sayap":10000}


def tro():
	for i in "kalkulator sederhana untuk berjualan \n kode by- Dheans\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.04)

def pr():	
	print("="*30)
	print("GEROBAK CICKEN".center(29,"="))
	print("="*30)
	print(" =\tD.\t Dada \t 15.000 =".ljust(26,"="))
	print(" =\tP. \t Paha \t 20.000 =".ljust(27,"="))
	print(" =\tS. \t Sayap \t 10.000 =".ljust(28,"="))
	print(" =\tQ. \t Quit \t Exit =".ljust(29,"="))
	print(" =\tSum. \t Total Belanja =".ljust(30,"="))
	print("="*30,"\n")

def proses(x,y,z):
	print("\n\tAnda Membeli %s Sejumlah %d Potong"%(x,y))
	print("\tTotal %d"%z)
	print("="*30)
	
def total():
	print()
	print("\t","="*30)
	print("\t","= Total Belanja %d ".center(28, "=")%sum(kode))
	print("\t","="*30)
	print()
	kode.clear()

def user():
	while True:
		try:
			x=input("Masukan Nama atau Kode : \t")
			if x== "q" or x== "Q":
				break
			elif x== "sum" or x== "Sum":
				total()
				pr()
			else:
				y=int(input("Masukkan Jumlah Potong : \t"))
		except:
			print("\n\t\tMasukkan Angka, Ulangi!")
			continue
		if x == "Dada" or x == "dada" or x == "D" or x == "d":
			proses(x,y,y*pesanan["Dada"])
			kode.append(y*pesanan["Dada"])
			
		elif x == "Paha" or x == "paha" or x == "P" or x == "p":
			proses(x,y,y*pesanan["Paha"])
			kode.append(y*pesanan["Paha"])
			
		elif x == "Sayap" or x == "sayap" or x == "S" or x == "s":
			proses(x,y,y*pesanan["Sayap"])
			kode.append(y*pesanan["Sayap"])
			
tro()				
pr()
user()