data=[]
qty=[]
	
t=1
while t>0:

	barang=input("Nama_Barang %d :"%t)
	if barang =="q":
		break
	else:
		harga =int(input("Harga : "))
		jumlah=int(input("Jumlah pembelian : "))
		print()

		data.append([barang,harga])
		qty.append(jumlah)
	t +=1
semua =0
for x in range(len(qty)):
	nama=data[x][0]
	harga=data[x][1]
	unit=qty[x]
	total=unit*harga
	semua +=total

	print()
	print("Nama Barang :@_%s"%nama)
	print("\tHarga : %d Unit : %d "%(harga,unit))
	print("\t\tTotal : %6d"%total)
print()
print("_________________________")
print("Total Yang Harus dibayar : %d"%semua)
print("_________________________")
