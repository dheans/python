from tkinter import *
from tkinter import messagebox

app=Tk()
app.geometry("650x1015")
app.title("Data Entri Siswa")

def save():
	messagebox.showinfo("SAVE","Data have been saved")
	with open ("/storage/emulated/0/Data.txt","a+") as g:
		data=[]
		for i in [Nama1.get(),Alamat1.get(),Kelamin1.get(),Pendidikan1.get(),Wali1.get(),Tgl1.get(),Bln1.get(),Tahun1.get()]:
			data.append(i)
		g.write(data[0]+" : "+str(data))
		g.write("\n\n")
		g.close()
		hasil.configure(text=" TERSIMPAN!")
	
def clr():
	Nama1.delete(0,END)
	Alamat1.delete(0,END)
	Kelamin1.delete(0,END)
	Pendidikan1.delete(0,END)
	Wali1.delete(0,END)
	Tgl1.delete(0,END)
	Bln1.delete(0,END)
	Tahun1.delete(0,END)

Nama=Label(app,text="Nama")
Nama.place(x=10,y=50)

Alamat=Label(app,text="Alamat")
Alamat.place(x=10,y=150)

Kelamin=Label(app,text="Jenis Kelamin")
Kelamin.place(x=10,y=250)

Pendidikan=Label(app,text="Pendidikan Terakhir")
Pendidikan.place(x=10,y=350)

Wali=Label(app,text="Nama Wali")
Wali.place(x=10,y=450)

Tgl=Label(app,text="Tanggal Lahir")
Tgl.place(x=10,y=550)

Bln=Label(app,text="Bulan Lahir")
Bln.place(x=10,y=650)

Tahun=Label(app,text="Tahun Lahir")
Tahun.place(x=10,y=750)

hasil=Label(app,text="")
hasil.place(x=250,y=800)

Nama1=Entry(app,width=22)
Nama1.place(x=300,y=50)

Alamat1=Entry(app,width=22)
Alamat1.place(x=300,y=150)

Kelamin1=Entry(app,width=22)
Kelamin1.place(x=300,y=250)

Pendidikan1=Entry(app,width=22)
Pendidikan1.place(x=300,y=350)

Wali1=Entry(app,width=22)
Wali1.place(x=300,y=450)

Tgl1=Entry(app,width=22)
Tgl1.place(x=300,y=550)

Bln1=Entry(app,width=22)
Bln1.place(x=300,y=650)

Tahun1=Entry(app,width=22)
Tahun1.place(x=300,y=750)

boo=Button(app,command=save,text="Simpan",bg="red",width=12)
boo.place(x=200,y=850)

boo=Button(app,command=clr,text="Hapus",bg="blue",width=12)
boo.place(x=200,y=950)


app.mainloop()