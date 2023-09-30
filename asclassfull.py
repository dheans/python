
class Madrasah:
	nama_madrasah = "Assholihiyah"
	alamat_madrasah = "Lingkok Lekong"
	npwp = 98983992
	
	def info(self):
		return f"{self.nama_madrasah}"


class Pendiri(Madrasah):
	def __init__(self, nama_pendiri):
		self.nama_pendiri = nama_pendiri
	
	def info(self):
		return f"{self.nama_pendiri}"


class Organisasi(Madrasah):
	def __init__(self, kamad, wakamad, sekretaris, bendahara):
		self.kamad = kamad
		self.wakamad = wakamad
		self.sekretaris = sekretaris
		self.bendahara = bendahara
	def info(self):
		return f"{self.__dict__}"

	
class Karyawan(Madrasah):
	jumlah_karyawan = 0
	def __init__(self, nama, alamat, kelamin, lulusan, jabatan=""):
		self.nama = nama
		self.alamat = alamat
		self.kelamin = kelamin
		self.lulusan = lulusan
		self.jabatan = jabatan
		Karyawan.jumlah_karyawan += 1
		
	def set_jabatan(self,posisi):
		self.jabatan = posisi
		
	def info(self):
		return f"{self.nama} => {self.jabatan}"


class Guru:
	def __init__(self, nama, mapel, jam):
		self.nama = nama
		self.mapel = list(mapel)
		self.jam = jam
		self.jam_pelajaran = 35
		self.durasi_mengajar = jam*self.jam_pelajaran
	
	def __repr__(self):
		return f"{self.__dict__}"


madrasah = Madrasah()
pendiri = Pendiri("Tgh. Abdul Qodir Jaelani")
struktur = Organisasi("Nursaleh.Spd","kurnaen,Spd", "Anwarul Masalik", "Tholib,Spd")
guru = Karyawan("Agus Musanif,Spd","Pesisok","L","S1","Guru")

agus = Guru("Agus Musanif,S.Pd",["B.Inggris","B.Asing"],30)

def show(data):
	for k,v in data.__dict__.items():
		print(f"{k} ==> {v}")

print(madrasah.info())
print("\nPendiri")
show(pendiri)
print("\nStruktur Organisasi")
show(struktur)
print("\nDetails Guru")
show(guru)
print("\nDetails Personal Guru")
show(agus)
