# Perpustakaan report using python

# making array to storing data

DATA = []

# function to modify data

def insert_data(nama, buku, tempo=0):
	d = {}
	d["nama"] = nama
	d["buku"] = buku
	d["tempo"] = tempo
	DATA.append(d)

def clear_data(nama):
	for data in DATA:
		if data["nama"] == nama:
			DATA.remove(data)
			


insert_data("ilma","sejarah",9)
insert_data("hulwa", "biologi")
insert_data("zahra", "logi")

print(DATA)
print()
clear_data("hulwa")

for data in DATA:
	print(data)