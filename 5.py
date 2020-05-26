def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
print(countdown(5))

print("5.1")
import time
import datetime

print(time.time())

print(datetime.datetime.now())

def ti(min):
    return all/min


all = time.time()

print(ti(60))
print(ti(60*60))
print(int(ti(60*60*12)))


print("5.2")

def check_fermat(a, b, c, n):

    if n>=2 and  a**n+b**n==c**n:
        print("fermat was wrong")
    else:
        print("correct")

print(check_fermat(1,0,1,3))


print("5.3")

def triangle(a,b,c):
    if a+b>c:
        print("is triangle")
    elif a+c>b:
        print("is triangle")
    elif c+b>a:
        print("is triangle")
    else:
        print("is not")

print(triangle(1,2,2))

def tri(d,e,f):
    if d+e>f or d+f>e or e+f>d:
        print("true")
    else:
        print("F")

print(tri(1,2,2))

print("5.4")

def r(n,s):
    '''

    :param n:
    :param s:
    :return:
    '''
    if n==0:
        print(s)
    else:
        r(n-1,n+s)

print(r(3,0))




