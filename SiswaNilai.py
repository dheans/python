"""Sample OOP """

class siswa:
	"""Membuat Data Siswa """
	
	def __init__(self,nama,nis,mapel):
		self.nama = nama
		self.nis = nis
		self.mapel = mapel
		self.nil =[]
		self.rata = 0
		self.total = 0
		
	def show(self):
		print()
		print("STUDENT DETAIL")
		print("\tNama : %s"%self.nama.title())
		print("\tNIS : %d"%self.nis)
		print("\tNilai : %d"%self.total)
		print("\tRata-rata : %.2f"%self.rata)
		
	def nilai(self):
		t=[]
		for x in range(self.mapel):
			ni=int(input("Input Nilai %d : "%int((x+1))))
			self.total += ni
			t.append(ni)
		self.nil += t
		self.rata += self.total/self.mapel
	

T=True
dt=[]
while T:
	print("\t\tq to quit".upper())
	print()
	print("Nama :")
	Nama= input("\t")
	if Nama == "q":
		T=False
	else :
		NIS= int(input("Nis : "))
		Mapel= int(input("Jumlah Mapel : "))
		Siswa=siswa(Nama,NIS,Mapel)
		Siswa.nilai()
		Siswa.show()
	
		dt.append(Siswa.__dict__)
for data in dt:
	for k,v in data.items():
		print(k,"++",v)