class uangmasuk:

    def __init__(self, jumlah, belanja, sisa=0):
        self.jumlah = jumlah
        self.belanja = belanja
        self.sisa = self.jumlah - self.belanja

    def __repr__(self):
        return f" Jumlah Uang : {self.jumlah}\n Jumlah belanja : {self.belanja}\n"


print("Sample code to create depo and credit amount")
print()
print("==" * 20)
print()
deposit = int(input("insert amount your depo : "))

while deposit:

    kredit = int(input("insert your credit : "))
    if kredit == 0:
        print("your balance :")
        print(saldo.sisa)
        break
    saldo = uangmasuk(deposit, kredit)
    deposit = saldo.sisa

    print(saldo)
    print(">>" * 20)
    print(" Sisa depo : ", saldo.sisa)
