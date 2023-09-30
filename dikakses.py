siswa=[{"name": "andi","nis":187873,"alamat":"Terara","Jenis Kelamin": "L"},{"name":"ania","nis":26465,"alamat":"Santong","Jenis Kelamin":"P"}]
#y="name"



def cari(a):
	for y in range(len(siswa)):
		for i,j,k,l in siswa:
			if a in siswa[y][i]:
				return "Nama %s \n\tDengan No Induk %d \n\tAlamat %s \n\tJenis Kelamin %s"%(a,siswa[y][j],siswa[y][k],siswa[y][l])
			

				
								
													

while True:
	i= input("masukkan nama siswa : ")
	a=cari(i)
	print(a)
