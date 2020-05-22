print("4.3.4+5")
import turtle
import math
bob = turtle.Turtle()
def circle(t,r,angle):
    length=math.pi*r*2/360
    for i in range(angle):
        t.fd(length)
        t.lt(360/360)
print(circle(bob,40,360))
