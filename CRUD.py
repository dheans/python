#CRUD

class Crud:
	"""jsjsjhsbsh """
	data=[]
	def __init__(self, nama):
		self.nama = nama
		dt={"nama":self.nama}
		Crud.data.append(dt)
	def Hapus(self):
		for x in Crud.data:
			if x["nama"] == self.nama :
				Crud.data.remove(x)

	def Edit(self,Other):
		for x in Crud.data:
			if x["nama"] == self.nama:
				self.nama = Other
				
	def __repr__(self):
		for x in Crud.data:
			for k,v in x.items():
				return f"{k} : {v}"
