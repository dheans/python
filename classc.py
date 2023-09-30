class crud:
    Data = []
    """ nama --> str
        alamat --> str
        kelamin --> str
        umur --> int """

    def __init__(self, **kwrg):
        self.kwrg = kwrg
        crud.Data.append(kwrg)

    def __repr__(self):
        for x in crud.Data:
            return f"{x}"
    def set(self):
        return "{!r}".format(self.__dict__)

d = crud(nama="dheans", alamat="sampang Tiga")
d = crud(nama="Ilma", alamat="sampang Tiga")
d = crud(nama="Hulwa", alamat="sampang Tiga")
t = crud(nama="Zahra", alamat="sampang Tiga")
print(crud.Data)
for x in d.Data:
    for k, v in x.items():
        print(f"{k} --- {v}")
print(d.set())
print(t.set())
