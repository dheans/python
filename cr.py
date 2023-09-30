Data = []

def masuk(**kwrg):
    Data.append(kwrg)

# Lookup data with nama
def show(arg):
    data =None
    for x in range(len(Data)):
        if Data[x]["nama"] == arg:
            data = "data ketemu"
            print(Data[x])

        else:
            if data ==None:
                data ="data tidak ketemu"
    print(data)

def showall():
    for data in Data:
        print(data)
masuk(nama = "alu",alamat="Sampang Tiga", Kelamin="L")
masuk(nama = "Ilma Hulwatuzzahra",alamat="Sampang Tiga", Kelamin="P")
masuk(nama = "Hulwa",alamat="Sampang Tiga", Kelamin="P")
masuk(nama = "Ilma",alamat="Sampang Tiga", Kelamin="P")

show("Ilma")
print()
show("alu")
show("Hulwa")

