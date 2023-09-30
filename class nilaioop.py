
class Nilai:
	daftar_nilai = []
	jumlah_siswa = 0
	def __init__(self,nama,*nilai):
		self.nama = nama
		self.nilai = nilai

#nilai partisipasi,tugas,uts dan uas
		self.__progres = [10,20,30,40]
		
#nilai ahir dikali nilai progress/100		
		self.nilai_progres = [self.nilai[x]*(self.__progres[x]/100) for x in range(4)]
		self.nilai_ahir=int(sum(self.nilai_progres))
		self.jumlah_nilai = sum(self.nilai)
		self.bobot = 0
		self.huruf = ""
		Nilai.daftar_nilai.append(self.jumlah_nilai)
		Nilai.jumlah_siswa += 1
	
#Menentukan bobot nilai
		if self.nilai_ahir >=92:
			self.bobot += 4.3
		elif self.nilai_ahir >= 90:
			self.bobot += 4
		elif self.nilai_ahir >= 85:
			self.bobot += 3.7
		elif self.nilai_ahir >= 80:
			self.bobot += 3.3
		elif self.nilai_ahir >= 75:
			self.bobot += 3
		elif self.nilai_ahir >= 70:
			self.bobot += 2.7
		elif self.nilai_ahir >= 65:
			self.bobot += 2.3
		elif self.nilai_ahir >= 60:
			self.bobot += 2
		elif self.nilai_ahir >= 50:
			self.bobot += 1
		else:
			self.bobot = 0
			
#menentukan nilai huruf
		if self.bobot == 4.3:
			self.huruf += "A+"
		elif self.bobot == 4:
			self.huruf += "A"
		elif self.bobot == 3.7:
			self.huruf += "A-"
		elif self.bobot == 3.3:
			self.huruf += "B+"
		elif self.bobot == 3:
			self.huruf += "B"
		elif self.bobot == 2.7:
			self.huruf += "B-"
		elif self.bobot == 2.3:
			self.huruf += "C+"
		elif self.bobot == 2:
			self.huruf += "C"
		elif self.bobot == 1:
			self.huruf += "D"
		elif self.bobot == 0:
			self.huruf = "E"	

	def __repr__(self):
		return f"{self.nama} \n\t Nilai Akhir : {self.nilai_ahir} \n\t Bobot Nilai : {self.bobot} \n\t Nilai Huruf : {self.huruf}\n"

#Ilma = Nilai("Ilma Hulwa",90,90,80,90)
#Kaila = Nilai("Kaila Vania",90,86,79,89)

Data=[]
n=int(input("Jumlah Siswa : "))
print("ket :")
print("Nilai 1 = Nilai Kehadiran/partisipasi")
print("Nilai 2 = Nilai Tugas")
print("Nilai 3 = Nilai Uts/Mid")
print("Nilai 4 = Nilai Uas/Semester")
print("\tNilai Akhir = \n\t\tNilai 1x10% + \n\t\tNilai 2x20% + \n\t\tNilai 3x30% + \n\t\tNilai 4x40%")
print()
for x in range(n):
	Nama=input("Masukkan Nama Siswa %d : "%(x+1)).title()
	Jawab=list(map(int,input("\tList Nilai : ").split()))
	
	partisipasi,tugas,uts,uas = Jawab

	Hasil = Nilai(Nama,partisipasi,tugas,uts,uas)
	Data.append(Hasil)
print()
for i in Data:
	print(i)
