class Animals:
	
	def __init__(self,chickens : int, cows : int, pigs : int):
		self.chicken = chickens
		self.cows = cows
		self.pigs = pigs
		self.chicken_legs = 2
		self.cows_legs = 4
		self.pigs_legs = 4
	def __repr__(self):
		return f"{self.chicken * self.chicken_legs}, {self.cows * self.cows_legs}, {self.pigs * self.pigs_legs} = ( {self.chicken * self.chicken_legs + self.cows * self.cows_legs + self.pigs * self.pigs_legs} legs ) totals"


kandang =Animals(2,3,5)
kandang2 = Animals(6,20,30)
print(kandang, kandang2, sep="\n")