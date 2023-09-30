class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        self.transport = 25000
        self.bonus = 0

    def __repr__(self):
        return f"{self.nama}-{self.gaji}"


class Gaji(Karyawan):
    def __init__(self, nama, jabatan="", hari=0, lembur=0):
        super().__init__(nama, 0)
        self.nama = nama
        self.hari = hari
        self.__lembur = lembur * 100000
        self.jabatan = jabatan.upper()

        # Gaji sesuai jabatan
        if self.jabatan == "DIREKTUR":
            self.gaji = 3000000
        elif self.jabatan == "STAFF":
            self.gaji = 2000000
        else:
            pass
        if self.hari > 24 and self.__lembur > 5:
            self.bonus = 500000

        self.trans_total = self.hari * self.transport
        self.gaji_total = self.gaji + self.bonus + self.trans_total + self.__lembur

    def __repr__(self):
        return f"{self.nama} @{self.jabatan}\
		\nGaji : {self.gaji},\
		\nBonus : {self.bonus},\
		\nLembur : {self.__lembur},\
		\nTransport : {self.trans_total},\
		\nTotal_Gaji : {self.gaji_total}"


#if __name__ == "__main__":
#    Gaji = Gaji("contoh")
Hadi=Gaji("Hadi Syaputra","STAFF",25,7)
Andi=Gaji("Andi Wijayanto","DIREKTUR",29,8)
print(Hadi,Hadi.__dict__,Andi,sep="\n\n")
