class Gaji:
    """ Menentukkan gaji pokok karyawan"""
    def __init__(self, nama, jabatan, jam_mengajar,gaji_pokok=15000):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji_pokok = gaji_pokok
        self.jam_mengajar = jam_mengajar
# mappings key <F5> to excute python program

    def __repr__(self):
       return f"{self.nama}--{self.jabatan}--{self.gaji_pokok}--{self.jam_mengajar}--{self.jam_mengajar*self.gaji_pokok}"
Data =[]
def hh(x,y,z):
    Data.append(Gaji(x,y,z))
hh("Agus", "Pembina Osis",12)
hh("Azwar Anas", "Operator",13)

print()
print("nama--jabatan--gaji_pokok--jam_mengajar--total")
print()
for v in Data:
    print(v)
