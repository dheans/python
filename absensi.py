from collections import Counter

#Sample absensi siswa, created using python
nama=[
	"ilma",
	"hulwa",
	"zahra",
	"joni",
	"adi",
	"pani",
	"azid",
	"azin",
	"liza",
	"jono",
	"kayla",
	"vania",
	"agustin"
	]
nama.sort()

print("ABSENSI SISWA KLS II")
print("____________________")
print("I = Izin\nS = Sakit\nA = Alpa\nX = Hadir")
print("____________________")
print()
r=[]
d=[]
ket={"i": "Izin",
	"I": "Izin",
	"S": "Sakit",
	"s": "Sakit",
	"A": "Alpa",
	"a": "Alpa",
	"x": "Hadir",
	"X": "Hadir"}

for i in nama:
	dt={}






	y=input(i +" : ").upper()
	if y in ket.keys():
		c=ket[y]
		dt.setdefault(i,c)
	else :
		continue
	d.append(y)
	r.append(dt)
print()
print("Daftar Siswa :")
for i in r:
	for k,v in i.items():
		print("\t{}--{}".format(k.ljust(7),v.rjust(7)))
u=Counter(d)
print()
print("Ket :")
print("\t  .__________________.")
print("\t+__________________+__+")
for x,y in u.items():
	if x == "X":
		print(f"\t|Siswa yang Hadir: |{y:2}|")
	elif x == "I":
		print(f"\t|Siswa yang Izin : |{y:2}|")
	elif x == "S":
		print(f"\t|Siswa yang Sakit: |{y:2}|")
	else :
		print(f"\t|Siswa yang Alpa : |{y:2}|")
print("\t+__________________+__+")

