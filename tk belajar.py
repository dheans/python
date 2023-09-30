#semoga bermanfaat. wkwkwkwk
 
from tkinter import *
 
class DemoListbox:
    def __init__(self, parent, title):
        self.parent = parent
 
        self.parent.title(title)
        #self.parent.geometry("600x400")
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
 
        self.dataSiswa = (
            ["1", "Ilma Hulwa", "Terara", "+6281-672541", "II Mts"],
            ["2", "Kayla Vania", "Terara", "+6281-435271", "II Mts"],
            ["3", "Yazid Gunawan", "Terara", "+6281-123456", "II Mts"],
            ["4", "Murniatun", "Terara", "+6281-234567", "II Mts"],
            ["5", "Miftahul Jannah", "Terara", "+6281-213212", "II Mts"],
            ["6", "Ari", "Terara", "+6281-343434", "I Mts"],
            ["7", "Erik Kurniawan", "Terara", "+6281-212121", "II Mts"],
            ["8", "Isriani", "Terara", "+6281-567489", "I Mts"],
            ["9", "Azila Nur", "Terara", "+6281-867855", "II Mts"],
            ["10", "Nuraini", "Terara", "+6281-555432", "II Mts"],
            ["11", "Khaeria Awalia", "Terara", "+6281-111121", "II Mts"],
            ["12", "Ahmad Yusuf", "Terara", "+6281-768594", "II Mts"],
            ["13", "Andi Alfi", "Terara", "+6281-536829", "III Mts"],
            ["14", "M Denis", "Terara", "+6281-986794", "II Mts"],
            ["15", "Den Bagus", "Terara", "+6281-324689", "III Mts"])
 
        self.aturKomponen()
        self.aturKejadian()
        self.isiListbox()
        self.isiData()
 
        self.listboxData.focus_set()
 
    def aturKejadian(self):
        self.listboxData.bind('<ButtonRelease-1>', self.onKlikLB)
        self.listboxData.bind('<KeyRelease>', self.onKlikLB)
 
    def onKlikLB(self, event=None):
        self.isiData()
 
    def isiData(self):
        indeks = self.listboxData.curselection()
        kode = int(indeks[0])
 
        # hapus data
        self.entNomor.delete(0, END)
        self.entNama.delete(0, END)
        self.entAlamat.delete(0, END)
        self.entTelp.delete(0, END)
        self.entKelas.delete(0, END)
 
        # isi data
        self.entNomor.insert(END, self.dataSiswa[kode][0])
        self.entNama.insert(END, self.dataSiswa[kode][1])
        self.entAlamat.insert(END, self.dataSiswa[kode][2])
        self.entTelp.insert(END, self.dataSiswa[kode][3])
        self.entKelas.insert(END, self.dataSiswa[kode][4])
 
    def isiListbox(self):
        for dat in range(len(self.dataSiswa)):
            self.listboxData.insert(END, self.dataSiswa[dat][1])
 
        self.listboxData.selection_set(0)
 
    def aturKomponen(self):
        mainFrame = Frame(self.parent)
        mainFrame.pack(fill=BOTH, expand=YES)
 
        self.statusBar = Label(mainFrame, text="GUI ON PYDROID",
                               relief=SUNKEN, bd=1)
        self.statusBar.pack(side=BOTTOM, fill=X)
 
        # frame_kiri
        fr_kiri = Frame(mainFrame, bd=10)
        fr_kiri.pack(fill=BOTH, expand=YES, side=LEFT)
 
        scroll = Scrollbar(fr_kiri, orient=VERTICAL)
        self.listboxData = Listbox(fr_kiri, width=30,
                                   yscrollcommand=scroll.set)
 
        self.listboxData.pack(fill=Y, side=LEFT)
        scroll.configure(command=self.listboxData.yview)
        scroll.pack(side=LEFT, fill=Y)
         
 
        # frame_kanan
        fr_kanan = Frame(mainFrame, bd=10)
        fr_kanan.pack(fill=BOTH, expand=YES, side=RIGHT)
 
        # fr_kanan_atas
        fr_katas = Frame(fr_kanan)
        fr_katas.pack(side=TOP, expand=YES)
 
        # data Nomor
        Label(fr_katas, text='Nomor Urut').grid(
            row=0, column=0, sticky=W)
        self.entNomor = Entry(fr_katas)
        self.entNomor.grid(row=0, column=1)
 
        # data Nama
        Label(fr_katas, text='Nama Lengkap').grid(
            row=1, column=0, sticky=W)
        self.entNama = Entry(fr_katas)
        self.entNama.grid(row=1, column=1)
 
        # data Alamat
        Label(fr_katas, text='Alamat').grid(
            row=2, column=0, sticky=W)
        self.entAlamat = Entry(fr_katas)
        self.entAlamat.grid(row=2, column=1)
 
        # data NoTelp
        Label(fr_katas, text='No. Telp').grid(
            row=3, column=0, sticky=W)
        self.entTelp = Entry(fr_katas)
        self.entTelp.grid(row=3, column=1)
 
        # data Kelas
        Label(fr_katas, text='Kelas').grid(
            row=4, column=0, sticky=W)
        self.entKelas = Entry(fr_katas)
        self.entKelas.grid(row=4, column=1)
 
        # fr_kanan_bawah
        fr_kawah = Frame(fr_kanan)
        fr_kawah.pack(side=BOTTOM, expand=YES)
 
        self.btnAwal = Button(fr_kawah, text='<<',
                                   command=self.onAwal, width=5)
        self.btnAwal.pack(side=LEFT)
         
        self.btnPrev = Button(fr_kawah, text='<',
                                   command=self.onPrev, width=5)
        self.btnPrev.pack(side=LEFT)
 
        self.btnNext = Button(fr_kawah, text='>',
                                   command=self.onNext, width=5)
        self.btnNext.pack(side=LEFT)
         
        self.btnAkhir = Button(fr_kawah, text='>>',
                                   command=self.onAkhir, width=5)
        self.btnAkhir.pack(side=LEFT)
 
    def onAwal(self, event=None):
        datIndex = self.listboxData.curselection()
 
        self.listboxData.selection_clear(int(datIndex[0]))
        self.listboxData.selection_set(0)
        self.listboxData.activate(0)
         
        self.isiData()
     
    def onPrev(self, event=None):
        datIndex = self.listboxData.curselection()
 
        if int(datIndex[0]) == 0:
            pass
        else:
            self.listboxData.selection_clear(int(datIndex[0]))
            self.listboxData.selection_set(int(datIndex[0])-1)
            self.listboxData.activate(int(datIndex[0])-1)
         
            self.isiData()
     
    def onNext(self, event=None):
        jumDat = len(self.dataSiswa)
        datIndex = self.listboxData.curselection()
 
        if int(datIndex[0]) == jumDat-1:
            pass
        else:
            self.listboxData.selection_clear(int(datIndex[0]))
            self.listboxData.selection_set(int(datIndex[0])+1)
            self.listboxData.activate(int(datIndex[0])+1)
         
            self.isiData()
         
    def onAkhir(self, event=None):
        jumDat = len(self.dataSiswa)
        datIndex = self.listboxData.curselection()
 
        self.listboxData.selection_clear(int(datIndex[0]))
        self.listboxData.selection_set(jumDat-1)
        self.listboxData.activate(jumDat-1)
         
        self.isiData()        
     
    def onKeluar(self, event=None):
        self.parent.destroy()
 
if __name__ == '__main__':
    root = Tk()
 
    aplikasi = DemoListbox(root, "Demo Listbox - Aplikasi Data di Python")
 
    root.mainloop()