print("4.3.1+2")
import turtle
bob = turtle.Turtle()
def squre(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
print(squre(bob,50))

print("4.3.3")
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
print(polygon(bob,60,5))