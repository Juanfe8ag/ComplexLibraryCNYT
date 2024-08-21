import math

def sumarc(a,b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real,imag)


def restarc(a,b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real,imag)


def multiplicarc(a,b):
    real = a[0]*b[0] - a[1]*b[1]
    imag = a[0]*b[1] + b[0]*a[1]
    return (real,imag)


def dividirc(a,b):
    real = ((a[0]*b[0]) + (a[1]*b[1])) / ((b[0]**2) + (b[1]**2))
    imag = ((b[0]*a[1]) - (a[0]*b[1])) / ((b[0]**2) + (b[1]**2))
    return (real,imag)


def modulo(a):
    return ((a[0]**2) + (a[1]**2))**(1/2)


def conjugado(a):
    return (a[0],-a[1])


def polar(a):
    p = modulo(a)
    teta = fase(a)
    return (p,teta)


def cartesiano(a):
    x = a[0]*math.cos(a[1])
    y = a[0]*math.sin(a[1])
    return (x,y)


def fase(a):
    if a[0] == 0 and a[1] > 0:
        return math.pi/2
    elif a[0] == 0 and a[1] < 0:
        return (3*math.pi)/2
    else:
        return math.atan(a[1]/a[0])


def prettyprint(a):
    if a[1] > 0:
        print(round(a[0],2),' + ',round(a[1],2),'i')
    elif a[1] == 0:
        print(round(a[0], 2))
    else:
        print(round(a[0], 2), ' - ', round(-1*a[1], 2),'i')

prettyprint(sumarc((2.3,4.6),(1.4,5.3)))
prettyprint(restarc((0.7, 2.7), (0.7, 2.7)))
prettyprint(multiplicarc((4, -2.3), (1.6, 3)))
prettyprint(dividirc((5,-2),(3,1)))
print(modulo((3,4)))
prettyprint(conjugado((6,7)))
print(polar((0, 1)))
prettyprint(cartesiano((5,math.pi/2)))
print(fase((4,4)))