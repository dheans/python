ket={
	0 : "mtk",
	1 : "bahasa",
	2 : "pisika",
	3 : "Qur'an Hadits",
	4 : "Fikih",
	5 : "Sosiologi",
	6 : "Geograpi",
	7 : "Kimia",
	8 : "Asing",
	9 : "Penjas",
	"doble" : "DOBEL"
}

#print(ket)
print()
senin=list(range(4))
selasa=list(range(1,5))
rabu=list(range(2,6))

y,x,z=senin,selasa,rabu
#print(x,y,z)
for e,i in enumerate(y):
		if y[e] == z[e] or y[e] == x[e] :
			y[e] = "doble"
			if i in x:	
				print(ket[i],"Senin,Selasa Dobel",sep="\n\t")
			elif i in z:
				print(ket[i],"Senin,Rabu Dobel",sep="\n\t")

		#else:
			#print()
			#ket[y[e]]
print()
sen=[7,6,8,9]
print()
o=[ket[y[i]] for i in range(len(y))]
print("Senin :",o)
print()
p=[ket[x[i]] for i in range(len(x))]
print("Selasa :",p)
print()
r=[ket[z[i]] for i in range(len(z))]
print("Rabu :",r)
