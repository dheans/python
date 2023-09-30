from time import sleep
#lis=["a","b","c","d","b","a","b","d","d","a","b","c"]
lis=input("Masukkan Kunci Jawaban : ").upper()
print("KUNCI JAWABAN : \n\t.  ",list(lis))
print("="*30)
f=0
while True:
	f+=1
	los=input("Masukkan List Jawaban  Siswa ==> %d : "%f).upper()
	los=list(los[:len(lis)])
	hasil=[]
	for i in range(len(lis)):
		soal,jawab=lis[i],los[i]
	
		if jawab==soal:
			print("_jawaban %s no. %d ✓"%(soal,i+1))
			hasil.append(jawab)
	
		else:
			print("\t\t_jawaban %s no. %d X"%(jawab,i+1))
		sleep(0.03)
	if len(hasil)>=(len(lis)/2):
		s="Selamat, Siswa ke %d 'Lulus'"%f
	else:
		s="Silahkan Belajar Lebih Giat Lagi"
	print("\njumlah jawaban benar : ",len(hasil))
	print("jumlah jawaban salah : ",len(lis)-len(hasil))
	print("° "*20)
	print("Nilai Siswa Ke ", f ," : \t %.2d.0"%(len(hasil)*(100/len(lis))),s)
	print("Code by d-heans".rjust(60))
	print()
