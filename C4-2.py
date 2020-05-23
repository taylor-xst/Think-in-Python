import turtle
import math


def circle(t,r,angle):
    """
    :param t: XXX
    :param r: XXX
    :param angle: XXX
    :return: None
    """

    length=math.pi*r*2/360
    for i in range(angle):
        t.fd(length)
        t.lt(360/360)


if __name__ == '__main__':
    print("4.3.4+5")

    bob = turtle.Turtle()
    print(circle(bob, 40, 360))