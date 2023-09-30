from random import choice

su=["t","i","k"]

print("_"*11)
print("|","telunjuk as t")
print("|","ibu jari as i")
print("|","kelingking as k")
print("|_","_"*9)
print("kesempatan anda hanya (5)")
print()

class b:
	men=0
	kal=0
	dr=0	
	def menang(self):
		print("anda menang")
		print("computer memilih %s, anda memilih %s "%(ai,user))
		print("sisa nyawa %d"%int(live-1))
		b.men += 1
		print("menang: ",b.men,"kalah: ",b.kal,"drow: ",b.dr)
		print()

	def kalah(self):
		print("anda kalah")
		print("computer memilih %s, anda memilih %s"%(ai,user))
		print("sisa nyawa %d"%int(live-1))
		b.kal +=1
		print("menang: ",b.men,"kalah: ",b.kal,"drow: ",b.dr)
		print()

	def drow(self):
		print("drow")
		print("computer memilih %s, anda memilih %s"%(ai,user))
		print("sisa nyawa %d"%int(live-1))
		b.dr +=1
		print("menang:",b.men,"kalah: ",b.kal,"drow: ",b.dr)
	
		print()
		
us=b()
live=int(input("MAU BERAPA KALI SUT  "))
while live :
	ai=choice(su)
	user=input("insert choice :  ")
	print()
	if ai =="t":
		if user == "i":
			us.menang()
		elif user =="k":
			us.kalah()
		elif user=="t":
			us.drow()
	if ai== "i":
		if user== "k":
			us.menang()
		elif user== "t":
			us.kalah()
		elif user =="i":
			us.drow()
	if ai=="k":
		if user== "t":
			us.menang()
		elif user =="i":
			us.kalah()
		elif user == "k":
				us.drow()
	live -=1

	