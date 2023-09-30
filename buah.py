import time


buah = int(input("masukan jumlah buah : "))
tan = float(input("masukan jumlah tan : "))
jumlah = float(buah/tan)
harga = 38
bonus = 10

if jumlah >= 48:
    bous = 17.5
elif jumlah >= 45:
    bonus = 15.5
elif jumlah >= 35:
    bonus = 15
elif jumlah >= 25:
    bonus = 14.5
else :
    bonus = 10

gaji = jumlah*harga
bonus = jumlah*bonus
for i in range(15):
    print("°•°"*i)
    time.sleep(i-i+0.02)
# skrip menghitung gaji sawit.

print("\t_jumlah tan anda : %0.2f Tan" % (buah/tan))
print("\t_jumlah gaji anda : %0.2f Rm" % (gaji))

print("\t_jumlah bonus anda : %0.2f Rm" % (bonus))
print(" ~"*25)
print("\t_TOTAL :.      %0.2f , KAN LUEK WAH TIE" % (gaji+bonus))
