# Hailey Tyler
# Graphics Lab
# 3-14-19

import graphics
win = graphics.GraphWin()
win.close()

from graphics import *
win = GraphWin()
win.close()

p = Point(50,60)
p.getX()
p.getY()
win = GraphWin()
p.draw(win)
p2 = Point(140,100)
p2.draw(win)

#### Open a graphics window
win = GraphWin('Shapes')
#### Draw a red circle centered at point (100,100) with radius 30
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
#### Put a textual label in the center of the circle
label = Text(center, "Red Circle")
label.draw(win)
#### Draw a square using a Rectangle object
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)
#### Draw a line segment using a Line object
line = Line(Point(20,30), Point(180, 165))
line.draw(win)
#### Draw an oval using the Oval object
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)

circ = Circle(Point(100,100), 30)
win = GraphWin()
circ.draw(win)

## Incorrect way to create two circles.
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye
rightEye.move(20,0)

## A correct way to create two circles.
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = Circle(Point(100, 50), 5)
rightEye.setFill('yellow')
rightEye.setOutline('red')

## Correct way to create two circles, using clone.
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye.clone() # rightEye is an exact copy of the left
rightEye.move(20,0)
win = GraphWin()
leftEye.draw(win)
rightEye.draw(win)

# pg.125-126 Exercise 3

from graphics import *

def main():
    win = GraphWin()
    shape = Circle(Point(50,50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    win.close()
main()
# click.py
from graphics import *

def main():
    win = GraphWin("Click me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
main()

# triangle.pyw
from graphics import*

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
main()
