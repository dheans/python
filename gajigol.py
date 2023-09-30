class Gaji:
	def __init__(self,nama,gol,lembur=0,pinjaman=0):
		self.nama = nama
		self.gol = gol
		self.lembur = lembur
		self.pinjaman = pinjaman
		self.gaji = 0
		self.cicilan =0
#menentukan gaji pokok dan gaji lembur sesuai golongan
		if self.gol in "A":
			self.gol = 10000
			self.gaji = 3000000
		elif self.gol in "B":
			self.gol = 11000
			self.gaji = 3100000
		elif self.gol in "C":
			self.gol = 12000
			self.gaji = 3200000
#menentukan cicilan perbulan
			
		if self.pinjaman > 1000000:
			self.cicilan = (self.pinjaman/10) * 3/100
		else:
			self.cicilan = self.pinjaman /10
			
	def __repr__(self):
		return f"Nama :{self.nama}\nGaji :{self.gaji} + Gaji_Lembur : {self.gol * self.lembur}\nPotongan :{self.cicilan}\nGaji diterima : {self.gaji - (self.cicilan) + (self.gol * self.lembur)}\n"
	
y=Gaji("Iwan","C",10,1000000)
i=Gaji("Budi","B",45)

print(y)
print(i)
		