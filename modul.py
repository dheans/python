class Assholihiyah:
	"""Instansi sekolah yang memuat semua data Madrasah Assholihiyah"""
	Total_Karyawan =0
	def __init__(self,Nama,Jabatan=None,Gaji=0):
		self.Nama = Nama
		self.Jabatan = Jabatan
		self.Gaji = Gaji
		Assholihiyah.Total_Karyawan += 1
		
	def __repr__(self):
		return f"{self.Nama}  @_{self.Jabatan}  Rp.{self.Gaji},-"
		
class Guru(Assholihiyah):
	Total_Guru = 0
	def __init__(self,Nama,Jabatan,Jam):
		super().__init__(Nama,Jabatan,15000)
		self.Gaji *= Jam
		Guru.Total_Guru +=1

u=Assholihiyah("Nursaleh,S.Pd","Kepala Madrasah",2000000)

Pak_Agus=Guru("Agus Musannif,S.Pd","Guru Mapel",100)
Pak_Tolib=Guru("Tholib,S.Pd","Wali Kelas",198)

print(u)
print("Total Instansi",Assholihiyah.Total_Karyawan)
print()
print(Pak_Agus)
print(Pak_Tolib)
print("Total Guru : ",Guru.Total_Guru)
