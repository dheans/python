t="aabbgggbhhcnnnf"
lis=[]
tmp=t[0]
for i in range(1,len(t)):
	if t[i] == t[i-1]:
	
		tmp += t[i]
	else :
		lis.append(tmp)
		tmp=t[i]
	if i == len(t)-1:
		lis.append(tmp)
		
	
	
		
		
print("\nbod".join([li for li in lis]))
	