print("5.6 koch")

import turtle


def draw(t, length, angle):
    if length >= 3:
        t.fd(length / 3)
        t.lt(angle)
        t.fd(length / 3)
        t.rt(angle)
        t.fd(length / 3)
        t.lt(angle)
        t.fd(length / 3)

    else:
        t.fd(length)


def snowflake(t, length, angle):
    for i in range(6):
        draw(t, 20, 60)
        t.rt(120)


bob = turtle.Turtle()

print(snowflake(bob, 50, 60))

turtle.mainloop()
