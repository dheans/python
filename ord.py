
i=int(input())
y=input()
class object:
	def __init__(self,o,c):
		self.o = o
		self.c = c
	def s(self):
		p=""
		for x in range(len(self.c)):
			k=ord(self.c[x])
			p += str(k)+" "
			print(chr(k))
	
		return " %s, %s"%(chr(self.o),p)
		
		
print(object(i,y).s())


