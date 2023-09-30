data=["Baju-25000-45",
	"Celana-52500-67",
	"Sepatu-15000-78"]


def stok_barang(barang,qty):
	print("\t+======================================+")
	print("\t|Nama\t |Jumlah|Harga/Unit|Total      |")
	print("\t+========+======+==========+===========+")
	i=0
	t=[]
	for k,v in barang.items():
		jumlah=qty[i]
		t.append(jumlah*v)
		print(f"\t|{k}\t |{jumlah:=4} \t| Rp.{v:>6}|Rp.{t[i]:>8}|")
		i +=1
	print("\t+========+======+==========+===========+")
	print(f"\tTOTAL BELANJA : Rp.{sum(t)}\n")
	print("\t_______________")
	uang=int(input("\tMasukkan Uang :Rp. "))
	print(f"\tKEMBALIAN : Rp.{uang-sum(t)}")

keranjang={}
jumlah_unit=[]
nu = 1
print("\t\tx to exit".upper())
while nu != 0:
	
	barang=input("(?) Nama Barang %d/X : "%nu)
	if barang in ("x","X"):
		break
	harga=int(input("(?) Harga/unit : "))
	jumla=int(input("(?) Jumlah Barang : "))
	keranjang.setdefault(barang,harga)
	jumlah_unit.append(jumla)
	print()
	nu +=1
nanya=input("(?) Print Struk,y/n : ")
print()
if nanya in ("y","Y"):
	stok_barang(keranjang,jumlah_unit)
	print("\tSenang Bertransaksi Dengan Anda".upper())
else:
	print("Bye")
