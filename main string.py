y="haji muhammad alpian".title()
h=""
for i in y:
	if i in y.upper():
		h+=i.replace(" ", "-")
print(h, end="")
