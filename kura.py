import turtle

win= turtle.Screen()
pen = turtle.Turtle()
win.bgcolor("black")

colors =["red","green","blue","orange","purple","yellow"]
#pen.goto(-160,-400)

def g(x,y):
	pen.pu()
	pen.goto(x,y)
	pen.pd()
	for i in range(50):
		#pen.goto((i/100)+2,(i/100)+2)
		pen.color(colors[i%6])
		pen.backward(i)
		pen.width(i/100+2)
		pen.right(59)
#		pen.circle(3+i,180)
		pen.speed(0)

#		pen.degrees(7)
for i in range(-300,400,100):
	g(-i,i)
	g(i,0)
	g(0,i)
	g(i,i)
win.mainloop()