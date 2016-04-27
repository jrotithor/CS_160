import turtle
window = turtle.Screen();
turtle = turtle.Turtle();
turtle.setheading(324);
def drawstar(x,y):
	turtle.clear();
	for x in range (0,5):
		turtle.forward(100);
		turtle.left(144);
		x += 1;
turtle.onclick(drawstar);
window.mainloop();
