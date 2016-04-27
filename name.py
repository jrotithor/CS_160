import turtle

window = turtle.Screen();
turtle = turtle.Turtle();
def j():
	turtle.penup();
	turtle.setpos(-150,0);
	turtle.pendown();
	turtle.setheading(180);
	turtle.forward(50);
	turtle.setheading(0);
	turtle.forward(25);
	turtle.right(90);
	turtle.forward(100);
	turtle.right(90);
	turtle.forward(25);
	turtle.penup();
def a():
	turtle.setheading(0);
	turtle.forward(50);
	turtle.pendown();
	turtle.forward(35);
	turtle.left(180);
	turtle.forward(10);
	turtle.right(90);
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(25);
	turtle.penup();
def z():
	turtle.setheading(0);
	turtle.forward(75);
	turtle.pendown();
	turtle.setheading(225);
	turtle.forward(35);
	turtle.setheading(45);
	turtle.forward(70);
	turtle.setheading(225);
	turtle.forward(35);
	turtle.setheading(135);
	turtle.forward(35);
	turtle.setheading(315);
	turtle.forward(35);
	turtle.penup();
def d():
	turtle.setheading(0);
	turtle.forward(50);
	turtle.pendown();
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(50);
	turtle.left(180);
	turtle.forward(25);
	turtle.right(90);
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(25);
	turtle.penup();
def e():
	turtle.setheading(0);
	turtle.forward(30);
	turtle.pendown();
	turtle.left(90);
	turtle.forward(30);
	turtle.right(90);
	turtle.forward(20);
	turtle.right(90);
	turtle.forward(15);
	turtle.right(90);
	turtle.forward(20);
	turtle.left(90);
	turtle.forward(15);
	turtle.left(90);
	turtle.forward(30);
	turtle.penup();



def p():
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(25);
	turtle.left(90);
	turtle.forward(50);
	turtle.penup();

def main(x,y):
	turtle.clear();
	j();
	a();
	z();
	d();
	e();
	e();
	p();
turtle.onclick(main);

window.mainloop();
